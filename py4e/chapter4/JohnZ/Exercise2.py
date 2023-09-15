input_number = input("Please enter a number between 0.0 and 1.0: ")

try:
    number = float(input_number)

    if number>= 0.6:
        final_number = "D"
        if number >= 0.7:
            final_number = "C"
            if number >= 0.8:
                final_number = "B"
                if number>= 0.9:
                    final_number = "A"
    elif 0<number < 0.6:
        final_number = "F"
except:
    print("Please enter float number")
    quit()
print(final_number)

