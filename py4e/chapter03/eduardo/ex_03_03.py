# Asks user for an score onput between 0.0 and 1.0
score_input = input("Enter score: ")

# handle a valid input
try:
    # parse number into a float value
    score = float(score_input)

    # check if the number is in the valid range
    if score < 0.0 or score > 1.0:
        print("Input must be between 0.0 and 1.0")
    
    # prints the score
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

# handles invalid inputs
except: 
    print("Input is not a number")
