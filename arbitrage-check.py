## Run individual process for each: USD, USDT, BUSD
## Needs to check if previous trade completed prior to starting new trade
## Trade trigger needs ability to perform all 3 trades in succession
## Needs connection to paper account for code testing and profitability verification
## Needs ability to cancel trades after timer
## Needs to be able to find sutible profit trades for failed 2nd and 3rd trades to prevent slippage and accidental holding
## Needs to compare if any better arrangements exist with the other primaries

from collections import defaultdict
from operator import itemgetter
from time import time
from datetime import datetime
from dotenv import load_dotenv
from binance import Client, ThreadedWebsocketManager
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException
import sys
import logging
import os

load_dotenv()

FEE = 0.0005
PRIMARY = ['USDT', 'BTC', 'USD', 'BUSD']
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
now = datetime.now()
client = Client(API_KEY, API_SECRET, tld='us')


def main():

    count = 0
    batch = 1

    log_start()
    size = os.stat('runlog.txt').st_size 

    if round(size / 1024) >= 100:
        with open('runlog.txt', 'w') as o:
            o.write('Log started: ' + str(now) + '\n')

    twm = ThreadedWebsocketManager(tld='us')

    twm.start()

    while count < 1001:
        count += 1

        start_time = time()
        prices = get_prices()
        pair = ''
        prices_time = time()
        print(f'Downloaded in: {prices_time - start_time:.4f}s')

        triangles = list(find_triangles(prices))
        print(f'Computed in: {time() - prices_time:.4f}s')
    
        
        if triangles:
            for triangle in sorted(triangles, key=itemgetter('profit'), reverse=True):
                describe_triangle(prices, triangle, batch, count, pair)
            break

        elif count <= 1000:
            print('No viable triangles found... Rechecking...', (str(count)+'/1000'))

        else:
            print('No viable triangles found in 1000 attempts.')
            count -= 1000
            with open('runlog.txt', 'a') as o:
                o.write(str('No viable triangles found in 1000 attempts. Batch #:' + str(batch)) + '\n')
            batch += 1

        if batch == 100:
            with open('runlog.txt', 'a') as o:
                o.write(str('Batch count exceeded. Restarting process... ' + str(now)) + '\n')
            main()


def log_start():
    with open('runlog.txt' ,'a') as o:
        o.write(str('PROCESS STARTED: ' + str(now)) + '\n')


def log_triangle(batch, count, trade_pairs, pair):
    with open('runlog.txt', 'a') as o:
        o.write(str('Triangle found batch #: ' + str(batch) + ' Attempt #: ' + str(count) +'/1000') + '\n')
        o.write(str('Viable Triangle:' + str(trade_pairs) + '' + str(now) + '\n' + str(pair)))
    

def get_prices():

    try:
       prices = client.get_orderbook_tickers()
    except BinanceAPIException as e:
        print(e.status_code)
        print(e.message)
        with open('runlog.txt', 'a') as o:
            o.write('API EXCEPTION! PROCESS HALTED ' + e.message + ' ' + e.status_code + '\n')
    else:    
        prepared = defaultdict(dict)
        for ticker in prices:
            pair = ticker['symbol']
            ask = float(ticker['askPrice'])
            bid = float(ticker['bidPrice'])
            if ask == 0.0:
                continue
            for primary in PRIMARY:
                if pair.endswith(primary):
                    secondary = pair[:-len(primary)]
                    prepared[primary][secondary] = 1 / ask
                    prepared[secondary][primary] = bid  
    return prepared


def find_triangles(prices):
    triangles = []
    starting_coin = 'USDT'
    for triangle in recurse_triangle(prices, starting_coin, starting_coin):
        coins = set(triangle['coins'])
        if not any(prev_triangle == coins for prev_triangle in triangles):
            yield triangle
            triangles.append(coins)


def recurse_triangle(prices, current_coin, starting_coin, depth_left=3, amount=1.0):
    if depth_left > 0:
        pairs = prices[current_coin]
        for coin, price in pairs.items():
            new_price = (amount * price) * (1.0 - FEE)
            for triangle in recurse_triangle(prices, coin, starting_coin, depth_left - 1, new_price):
                triangle['coins'] = triangle['coins'] + [current_coin]
                yield triangle
    elif current_coin == starting_coin and amount > 1.00025:
        yield {
            'coins': [current_coin],
            'profit': amount
        }


def describe_triangle(prices, triangle, batch, count, pair):
    trade_pairs = []
    coins = triangle['coins']
    price_percentage = (triangle['profit'] - 1.0) * 100
    print(f'{"->".join(coins):26} {round(price_percentage, 4):-7}% < Profit Yield')
    for i in range(len(coins) - 1):
        first = coins[i]
        second = coins[i + 1]
        trade_pairs.append(second + first)
        print(f'     {second:4} / {first:4}: {prices[first][second]:-17.8f}')
    print('')
    log_triangle(coins, batch, count, pair)
    define_pairs(trade_pairs, prices)

def define_pairs(trade_pairs, prices):
    symbols = []
    for primary in PRIMARY:
        for i in list(trade_pairs):
            if i.startswith(primary):
                secondary = i[:-len(primary)]
                print(secondary)
                symbols.append(secondary + primary)
            elif i.count('USDTUSD') == 1 or i.count('USDUSDT') == 1:
                symbols.append('USDTUSD')
            else:
                symbols.append(i)

    trade_pair_initial = str(symbols[0])
    trade_pair_second = str(symbols[1])
    trade_pair_final = str(symbols[2])

    trade_initial(prices, trade_pair_initial, trade_pair_second, trade_pair_final)

def trade_initial(prices, trade_pair_initial, trade_pair_second, trade_pair_final, twm):
    print( 'Initiating trade: ' + trade_pair_initial)

#    try: 
#        client.create_test_order(
#        symbol=str(trade_pair_initial), 
#        side='BUY', 
#        type='LIMIT', 
#        timeInForce='GTC', 
#        quantity=100, 
#        price=str(prices[trade_pair_final]))

#    except BinanceAPIException as e:
     #error handling goes here
#        print(e)
#    except BinanceOrderException as e:
     #error handling goes here
#        print(e)
    trade_secondary(prices, trade_pair_second, trade_pair_final, twm)   


def trade_secondary(prices, trade_pair_second, trade_pair_final, twm):
    print( 'Initiating trade: ', trade_pair_second)

#    try:
#        client.create_test_order(
#            symbol=trade_pair_second,
#            side='BUY',
#            type='LIMIT',
#            timeInForce='GTC',
#            quantity=100,
#            price=prices[trade_pair_second])

#    except BinanceAPIException as e:
     #error handling goes here
#        print(e)
#    except BinanceOrderException as e:
     #error handling goes here
#        print(e)
    trade_final(prices, trade_pair_final, twm)
    

def trade_final(prices, trade_pair_final, twm):
    print( 'Initiating trade: ', trade_pair_final)

#    try:
#        client.create_test_order(
#            symbol = trade_pair_final,
#            side = 'BUY',
#            type = 'LIMIT',
#            timeInForce = 'GTC',
#            quantity = 100,
#            price = prices[trade_pair_final])

#    except BinanceAPIException as e:
     #error handling goes here
#        print(e)
#    except BinanceOrderException as e:
     #error handling goes here
#        print(e)
    twm.stop()
    #main()
    

if __name__ == '__main__':
    main()