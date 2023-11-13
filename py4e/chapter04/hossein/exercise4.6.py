def computepay(hours:int, rate:float)->float:
    if hours<=40:
        pay = round(hours*rate, 2)
    elif hours>40:
        adjusted_pay = (40+ (hours-40)*1.5)*rate
        pay = round(adjusted_pay, 2)
    return pay


try:
    hours = input("Enter Hours: ")
    rate = input("Enter Rate: ")

    pay = computepay(int(hours), float(rate))

    print(f"Pay: {pay}")

except ValueError as err:
    print("Error, please enter numeric input")