score = input("Enter Score: ")

try:
    score = float(score)
    if score > 1:
        print("Error: Score inputed is greater than 1")
    elif score >= 0.9:
        print("A")    
    elif score >= 0.8:
        print("B")    
    elif score >= 0.7:
        print("C")    
    elif score >= 0.6:
        print("D")
    elif score >= 0:
        print ("E")
    else:
        print ("Error: Score inputed less than 0")
except :
    print ("Error: Score must be a numerical value")
