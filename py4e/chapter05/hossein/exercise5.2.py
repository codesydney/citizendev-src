maximum = float("-inf")
minimum = float("inf")
count = 0
total = 0
user_input=""

while user_input!="done":
    user_input: str = input("Enter a number: ")
    user_input = user_input.strip().lower()

    try:
        user_number = float(user_input)
    except ValueError as err:
        print("Invalid Input")
        continue
    
    count +=1
    total += user_number
    if user_number>maximum:
        maximum = user_number
    if user_number<minimum:
        minimum = user_number

if count > 0 :
    print(f"Total: {total}, Count: {count}, Max: {maximum}, Min: {minimum}")