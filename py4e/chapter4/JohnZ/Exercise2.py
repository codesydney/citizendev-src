input_number = input("Please enter a number between 0.0 and 1.0: ")


number = float(input_number)



if number >= 0.6:
    final_number = "D"
    if number >= 0.7:
        final_number = "C"
        if number >= 0.8:
            final_number = "B"
            if number >= 0.9:
                final_number = "A"
elif number < 0.6:
    final_number = "F"
print(final_number)

