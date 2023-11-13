def computegrade(score: float)->str:
    if score<0.0 or score>1:
        return "Bad score"
    if score<0.6:
        return "F"
    if score<0.7:
        return "D"
    if score<0.8:
        return "C"
    if score<0.9:
        return "B"
    return "A"


score = input("Enter score: ")

try:
    grade = computegrade(float(score))
    print(f"{grade}")

except ValueError as err:
    print("Bad score") 