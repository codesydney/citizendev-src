largest = float("-inf")
smallest = float("inf")

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num = float(num)
    except ValueError:
        print("Invalid input")
        continue

    largest = max(num, largest)
    smallest = min(num, smallest)

print("Maximum", largest)
print("Minimum", smallest)
