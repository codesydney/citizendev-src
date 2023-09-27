largest  = float('-inf')
smallest = float('inf')

while True:
    try:
        number = input('Enter a number: ')
        if number == 'done':
            break
        number  = int(number)
        #largest = int(largest)
        print(number)
    except:
        print('invalid input')
        continue

    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
print('Largest' ,  largest)
print('smallest' ,  smallest)


