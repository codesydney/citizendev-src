def computepay(hours, rate_per_hour):
    pay = 0
    if hours > 40:
        surplus_hours = hours - 40
        pay = pay + rate_per_hour * surplus_hours * 1.5
        hours = hours - surplus_hours
    pay = pay + hours * rate_per_hour
    return pay

hours = input("Enter Hours: ")
hours = float(hours)
rate_per_hour = input("Enter rate per hour: ")
rate_per_hour = float(rate_per_hour)
p = computepay(hours, rate_per_hour)
print("Pay", p)