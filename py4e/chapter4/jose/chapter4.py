def computepay(hours, rate):
    if hours > 40:
        excessRate  = rate * 1.5
        excessHours = hours - 40    
        basePay     = 40 * rate
        totalPay    = (excessHours * excessRate) + basePay
    else:
        totalPay    = float(hours) * float(rate)
    return totalPay
hours = input("Hours:")
rate = input("Rate:")
#recursion
paying = computepay(float(hours), float(rate))
print("pay" + " = " + str(paying))