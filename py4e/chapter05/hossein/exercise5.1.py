total = 0 
count = 0
average = 0
user_input=""

while user_input!="done":
    user_input: str = input("Enter a number: ")
    user_input = user_input.strip().lower()

    try:
        user_number = float(user_input)
    except ValueError as err:
        print("Invalid Input")
        continue

    total += user_number
    count += 1

if count>0:
    average = total/count
    print(f"Total: {total}, Count: {count}, Average: {average}")