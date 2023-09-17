hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

if float(hrs) > 40:
    excessrate = float(rate) * 1.5
    excesshrs = float(hrs) - 40    
    basepay = 40 * float(rate)
    grosspay = (excesshrs * excessrate) + basepay
else:
    grosspay = float(hrs) * float(rate)

print (grosspay)