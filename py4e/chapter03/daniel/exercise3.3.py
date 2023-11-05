score = input("Enter score between 1.0 and 0.0: ")

try:
    score = float(score)

    # Check for valid score
    if score > 1.0 or score < 0.0:
        print("Enter a valid range")
        quit()

    # Print grade
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
    else:
        print("Enter a valid score")

except ValueError:
    print("Enter a valid number")
    quit()