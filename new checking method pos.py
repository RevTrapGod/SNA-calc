def getMarketData(client, exclude):
    
    tickers = client.get_orderbook_tickers()
    
    for i in tickers:
        
        if 'USD' in i['symbol']:
            if i['symbol'].index('USD') != 0:
                i['symbol'] = i['symbol'].replace('USD','-USD')
                
        if 'BTC' in i['symbol']:
            if i['symbol'].index('BTC') != 0:
                i['symbol'] = i['symbol'].replace('BTC','-BTC')
        
        if 'BUSD' in i['symbol']:
            if i['symbol'].index('BUSD') != 0:
                i['symbol'] = i['symbol'].replace('BUSD','-BUSD')
        
        if 'USDT' in i['symbol']:
            if i['symbol'].index('USDT') != 0:
                i['symbol'] = i['symbol'].replace('USDT','-USDT')
        
    for i in tickers:
        if '-' not in i['symbol']:
            if 'USD' in i['symbol']:
                if i['symbol'].index('USD') != 0:
                    i['symbol'] = i['symbol'].replace('USD','-USD')
                    
            if 'BTC' in i['symbol']:
                if i['symbol'].index('BTC') != 0:
                    i['symbol'] = i['symbol'].replace('BTC','-BTC')
            
            if 'BUSD' in i['symbol']:
                if i['symbol'].index('BNB') != 0:
                    i['symbol'] = i['symbol'].replace('BUSD','-BUSD')
            
            if 'USDT' in i['symbol']:
                if i['symbol'].index('USDT') != 0:
                    i['symbol'] = i['symbol'].replace('USDT','-USDT')
    return tickers


