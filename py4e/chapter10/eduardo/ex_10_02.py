# prompt user to input the file name 
fname = input("Enter file name: ")

# try-except block to catch any user input errors
try:
    fh = open(fname)
except:
    print('The file cannot be opened:',fname)
    quit()

# Count dictionary to store hourly count of messages in emails starting with 'From '
counts = dict()
for each in fh:
    each = each.rstrip()
    if not each.startswith("From "):
        continue
    words = each.split()
    hour = words[5]

    # Slice (to get only the hour of the message) 
    hour = hour[:2]    
    counts[hour] = counts.get(hour, 0) + 1

# # Prints the key-value pairs in the counts list
for key,val in counts.items():
    print(key,val)

