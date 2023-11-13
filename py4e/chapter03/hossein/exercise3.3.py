# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

score = input("Enter score: ")

try:
    numeric_score = float(score)
    if numeric_score>1.0 or numeric_score<0.0:
        print("Bad Score")
    elif numeric_score >= 0.9:
        print("A")
    elif numeric_score>=0.8:
        print("B")
    elif numeric_score >= 0.7:
        print("C")
    elif numeric_score>=0.6:
        print("D")
    else:
        print("F")

except ValueError as err:
    print("Bad score") 