# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except FileNotFoundError:
    print("Invalid file name, please check your input and try again.")
    exit(0)

number_of_floating_point_values = 0
total_of_floating_point_values = 0.0


for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    floating_point_value = float(line[line.find(' '):])
    number_of_floating_point_values = number_of_floating_point_values + 1
    total_of_floating_point_values = total_of_floating_point_values + floating_point_value

fh.close()

average_of_floating_point_values = total_of_floating_point_values / number_of_floating_point_values

print(f"Average spam confidence: {average_of_floating_point_values}")
