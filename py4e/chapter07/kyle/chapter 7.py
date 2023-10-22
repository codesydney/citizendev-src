# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid file name")
    quit()
    
total = 0
num_spam = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    get_input = float(line[line.find(' ') :])
    total = get_input + total
    num_spam = num_spam + 1
        

print("Average spam confidence:", total/num_spam)
