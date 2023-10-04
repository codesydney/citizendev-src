hours = input("What is your hours?")
rate = input("What is your rate?")

if float(hours) > 40:
    penalty_rate_hours = float(hours) - 40
    normal_rate_hours = 40
    pay = normal_rate_hours * float(rate) + penalty_rate_hours * float(rate)*1.5     
else: 
    pay = float(hours) * float(rate)



print(pay)




