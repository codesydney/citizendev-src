score = float(input("Enter score between 0.0 and 1.0: "))

try:
    if score >= 1.0 or score < 0.0:
        print ('Please enter a valid range')
    elif score >= 0.9:
        print ('A')
    elif score >= 0.8:
        print ('B')
    elif score >= 0.7:
        print ('C')
    elif score >= 0.6:
        print ('D')
    else:
        print("F")
        
except ValueError:
    print("Please enter a valid number")
