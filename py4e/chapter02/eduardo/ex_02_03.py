# Program that uses input values of Hours and Rate per hour to calculate payments

# Input - Variables input
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

# Output/Print - Calculates and prints the total payment
payment = float(hours) * float(rate)
print("Pay:", payment)