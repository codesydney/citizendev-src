hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

hrs = float(hrs)
rate = float(rate)

# all hours are paid at regular rate
pay = hrs * rate

if hrs > 40.0:
    # just add the 50% overtime for extra hours
    pay = pay + ((hrs - 40.0) * (rate * 0.5))

print(pay)
