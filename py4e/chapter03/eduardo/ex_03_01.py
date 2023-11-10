# Ask user to prompt worked hours and hourly rate
hrs = input("Enter Hours: ")
rate = input("Enter hourly rate: ")

# handle a valid input
try:
    h = float(hrs)
    rate = float(rate)

    # Calculation for shift under 40 hrs
    if h <= 40:
        grossPay = h * rate
    # Calculation for shift above 40 hrs
    else:
        overtime = h - 40
        overtime_rate_factor = 1.5
        grossPay = (40 * rate) + (overtime * overtime_rate_factor * rate)
    
    print("The gross pay is: ", grossPay)

# handle an invalid input
except:

    print("Incorrect input. Restart the program and try again.")