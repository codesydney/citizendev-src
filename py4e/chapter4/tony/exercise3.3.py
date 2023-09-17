score = input("Enter Score: ")

try:
    score = float(score)

    if score > 1.0 or score < 0.0:
        print("Score must be between 0.0 and 1.0")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")

except ValueError:
    print("Did not enter a valid number")
