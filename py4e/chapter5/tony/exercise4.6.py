def compute_pay(hrs, rate):
    pay = hrs * rate
    if hrs > 40.0:
        pay = pay + ((hrs - 40.0) * (rate * 0.5))
    return pay


hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

print("Pay:", compute_pay(hrs, rate))
