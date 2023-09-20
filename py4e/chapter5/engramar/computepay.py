def computepay(h, r):
    if h > 40:
        excessrate = r * 1.5
        excesshrs = h - 40    
        basepay = 40 * r
        grosspay = (excesshrs * excessrate) + basepay
    else:
        grosspay = float(hrs) * float(rate)

    return grosspay

hours = input("Enter Hours:")
rate = input("Enter Rate:")

pay = computepay(float(hours), float(rate))

print("Pay", pay)

