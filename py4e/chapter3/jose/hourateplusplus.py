hours = input('Enter your hours:: ')
rate  = input('Enter your rate::  ')
if float(hours) > 40:
    excessRates = float(rate)  * 1.5
    excessHours = float(hours) - 40
    basePay     = 40 * float(rate)
    totalPay    = (excessHours * excessRates) + basePay
else:
    totalPay = float(hours) * float(rate)

print(totalPay)

