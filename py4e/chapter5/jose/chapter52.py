largest = None 
smallest = None 
while True: 
    num = input('Enter a number: ') 
    if num == 'done':
         break 
    else: 
        num = int(num) 
        print(num) 
        if largest == None or num > largest: 
           largest = num 
        elif smallest == None or num < smallest: 
             smallest = num 

if largest is not None: 
    print('largest ' , largest ) 
if smallest is not None: 
    print('Smallest ' , smallest) 
