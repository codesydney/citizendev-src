# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

total = 0
ctr = 0
ave = 0 
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue    
    atpos = line.find(':')
    num = line[atpos+1:len(line)]    
    total = total + float(num)
    ctr += 1    

ave = total / ctr
print ("Average spam confidence:",ave)