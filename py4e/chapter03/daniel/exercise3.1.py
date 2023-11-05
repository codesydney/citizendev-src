# Prompt user for hours and rate per hour
hours = float(input("Enter Hours: "))
wage = float(input("Enter Wage: "))

# Calculate pay
if hours <= 40:
    pay = hours * wage
else:
    pay = (40 * wage) + ((hours - 40) * (wage * 1.5))

# Print pay
print(pay)