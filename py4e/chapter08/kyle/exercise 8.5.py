fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    info = line.split()
    print(info[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
