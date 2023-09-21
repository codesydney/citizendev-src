# Test comment from JZ adfas
def computepay(c_hours,c_rate):

    if float(c_hours) > 40:
        penalty_rate_hours = float(c_hours) - 40
        normal_rate_hours = 40
        pay = normal_rate_hours * float(c_rate) + penalty_rate_hours * float(c_rate)*1.5     

    else: 
        pay = float(c_hours) * float(c_rate)

    return(f"Pay {pay}")

hours = input("What is your hours?")
rate = input("What is your rate?")

final_result = computepay(hours,rate)

print(final_result)
