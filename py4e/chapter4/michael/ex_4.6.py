#define computepay function
def computepay(hoursf, ratesf):
    if hoursf >40:
        pay = 40 * ratesf + (hoursf - 40) * ratesf * 1.5
    else: 
        pay = hoursf * ratesf
    return pay

#user value input
hrs = input ("Enter Hours:")
hrs = float(hrs)
rate = input ("Enter Rate:")
rate = float(rate)

#calling function and displaying output
p = computepay(hrs, rate)
print("Pay", p)
