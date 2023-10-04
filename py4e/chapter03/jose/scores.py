
try:
    score = float(input("Enter your score must between 0.0 and 1.0: "))
    if score >= 1.0 or score < 0.0:
        print ('Enter your range')
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
    print("Enter a valid number")
