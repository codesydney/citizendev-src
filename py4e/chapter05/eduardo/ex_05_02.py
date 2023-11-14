largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    
    try:
        
        if num == "done":
            print("Maximum is",largest)
            print("Minimum is",smallest)
            break
        
        num_user = int(num)

        if (smallest is None) or (num_user<smallest):
            smallest = num_user
        
        if (largest is None) or (num_user>largest):
            largest = num_user

    except:
        print("Invalid input")
        continue

