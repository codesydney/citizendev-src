largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num = float(num)
    except ValueError:
        print("Invalid input")
        continue

    largest = max(num, largest) if largest is not None else num
    smallest = min(num, smallest) if smallest is not None else num

print("Maximum", largest)
print("Minimum", smallest)
