# prompt user to input the file name 
fname = input("Enter file name: ")

# try-except block to catch any user input errors
try:
    fh = open(fname)
except:
    print('The file cannot be opened:',fname)
    quit()

# Count dictionary to store senders count of emails (in lines starting with 'From ')
counts = dict()
for each in fh:
    each = each.rstrip()
    if not each.startswith("From "):
        continue
    words = each.split()
    sender = words[1]
    counts[sender] = counts.get(sender, 0) + 1

# counts the most prolific committer
bigcount = 0
bigword = 0
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count 

# Print the most prolific committer
print(bigword, bigcount)