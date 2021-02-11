count = 0
#Get batch size
batch_size = input('Enter batch quantity in gallons: ')
#Validate input is num not alpha
while batch_size.isalpha()  == True or batch_size == '' or int(batch_size) > 9999:
    print('Invalid batch size. Batch size must be numeric.')
    batch_size = input('Enter batch quantity in gallons: ')
    count += 1
#Convert to int
batch_size = int(batch_size)

#Get yeast nutrient requirement
yeast_input = input('Enter yeast strain nutrient requirements\n(Low, Medium, High): ')
#Convert to consistent format
yeast_input = yeast_input.upper().strip()

#Define lsit to compare to
yeast_req = ['LOW', 'MEDIUM','HIGH']

#Validate input against list
while yeast_req.count(yeast_input) != 1:
    print('Yeast requirement must be "Low, Medium or High.')
    yeast_input = input('Enter yeast strain nutrient requirements\n(Low, Medium, High): ')
    #Convert to consistent format
    yeast_input = yeast_input.upper().strip()
    count += 1
    
#Convert batch size (Gal to L)
batch_size_l = batch_size*3.78541

#Get batch sg
sg = input('Enter batch SG: ')
while sg.isalpha()  == True or sg == '' or float(sg) > 2 or len(sg) != 6:
    print('Invalid SG. Ensure SG is in format X.XXXX')
    sg = input('Enter batch SG: ')
    count += 1

#Get Brix
brix = input('Enter batch Brix: ')
while brix.isalpha() == True or brix == '' or float(brix) > 99:
    print('Invalid Brix. Ensure brix is in format XX.X')
    brix = input('Enter batch Brix: ')
    count += 1

#Convert brix and sg to float
brix = float(brix)
sg = float(sg)

sugars = brix * sg * 10

yan_req = 0

if yeast_input == 'LOW':
    yan_req = sugars * 0.75
elif yeast_input == 'MEDIUM':
    yan_req = sugars * 0.90
elif yeast_input == 'HIGH':
    yan_req = sugars * 1.25

    
print(yeast_input + ' '+ str(batch_size_l) + ' ' + str(sg) + ' ' + str(brix) + 'º' + ' ' + str(sugars) + ' ' + str(yan_req))
