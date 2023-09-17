def compute_pay(hrs, rate):
    pay = hrs * rate
    if hrs > 40.0:
        pay = pay + ((hrs - 40.0) * (rate * 0.5))
    return pay


try:
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    if hrs <= 0.0 or rate <= 0.0:
        raise ValueError
    else:
        print("Pay:", compute_pay(hrs, rate))
        exit(0)

except ValueError:
    print("Hours and Rate must be numeric values greater than 0")
    exit(1)
