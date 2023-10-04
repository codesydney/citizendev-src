name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)

count = 0
d = dict()
for line in fh:
    if line.startswith("From:"):        
        email = line.strip().split(" ")        
        if email[1] not in d:
            d[email[1]] = 1
        else:
            d[email[1]] = d[email[1]] + 1

max_email = None 
max_count = 0 
for k,v in d.items():
    if v > max_count:
        max_email = k
        max_count = v

print(max_email, max_count)
fh.close()
