# Defined function to calculte workers payments
def computepay(workedHours, hourlyRate):
    
    h = float(workedHours)
    rate = float(hourlyRate)

    # Calculation for shift under 40 hrs
    if h <= 40:
        grossPay = h * rate
    # Calculation for shift above 40 hrs
    else:
        overtime = h - 40
        overtime_rate_factor = 1.5
        grossPay = (40 * rate) + (overtime * overtime_rate_factor * rate)
    
    print("The gross pay is: ", grossPay)

# Ask user to prompt worked hours and hourly rate
hrs = input("Enter Hours: ")
rate = input("Enter hourly rate: ")

# try-except block to catch any user input errors
try:
    computepay(hrs, rate)
except:
    print("Incorrect input. Restart the program and try again.")






