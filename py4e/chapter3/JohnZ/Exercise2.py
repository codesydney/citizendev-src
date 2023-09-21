input_number = input("Please enter a number between 0.0 and 1.0: ")

try: 
    number = float(input_number)

except:
    print("Please enter a number")
    quit()


if number >= 0 and number < 0.6:
    final_number = "F"
elif number>= 0.6 and number < 0.7:
    final_number = "D"
elif number >= 0.7 and number <0.8:
    final_number = "C"
elif number >= 0.8 and number <0.9:
    final_number = "B"
elif number>= 0.9 and number <=1:
    final_number = "A"
else:
    final_number = "Please enter a number between 0 and 1."

print(final_number)

