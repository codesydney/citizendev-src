largest = float('-inf')
smallest = float('inf')
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        num = int(num)
    except:
        print("Invalid input") 
        continue
        
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)