# prompt user to input the file name 
fname = input("Enter file name: ")

# try-except block to catch any user input errors
try:
    fh = open(fname)
except:
    print('The file cannot be opened:',fname)
    quit()

# Count variable to keep the number of lines with 'From ' on it
count = 0

for each in fh:
    each = each.rstrip()
    if not each.startswith("From "):
        continue
    count += 1
    line = each.split()

    # Print the email result in the line 
    print(line[1])    

# Print the total lines starting with 'From ' on it 
print("There were", count, "lines in the file with From as the first word")
