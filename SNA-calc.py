batch_size = input('Enter batch quantity in gallons:')
count = 0
#Check if format is correct
while batch_size.isalpha()  == True or batch_size == '':
    print('Batch size must be numeric.')
    batch_size = input('Enter batch quantity in gallons:')
    count += 1
#Convert to int
batch_size = int(batch_size)


yeast_input = input('Enter yeast strain nutrient requirements\n(Low, Medium, High):')
#Convert to consistent format
yeast_input = yeast_input.upper().strip()

#Define lsit to compare to
yeast_req = ['LOW', 'MEDIUM','HIGH']

#Compare to list
while yeast_req.count(yeast_input) != 1:
    print('Yeast requirement must be "Low, Medium or High.')
    yeast_input = input('Enter yeast strain nutrient requirements\n(Low, Medium, High):')
    #Convert to consistent format
    yeast_input = yeast_input.upper().strip()
    count += 1
    
print(yeast_input + ' '+ str(batch_size))