def computepay(h, r):
    if h <= 40:
        return h*r
    else:
        Overtime_hour = h - 40
        Overtime_rate = r*1.5
        return (40*r)+(Overtime_hour*Overtime_rate)

hours = input("Enter Hours:")
h = float(hours)

rate = input("Enter rate:")
r = float(rate)


p = computepay(h, r)


print("Pay", p)
