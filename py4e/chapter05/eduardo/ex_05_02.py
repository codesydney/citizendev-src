largest = None
smallest = None

# While loop definition
while True:
    num = input("Enter a number: ") # user input
    
    # try-except block to catch any user input errors
    try:
        
        if num == "done": # if statement to control the end of user inputs numbers
            print("Maximum is",largest)
            print("Minimum is",smallest)
            break
        
        num_user = int(num) # parse the input string into a integer

        if (smallest is None) or (num_user<smallest):
            smallest = num_user
        
        if (largest is None) or (num_user>largest):
            largest = num_user

    except:
        print("Invalid input")
        continue

