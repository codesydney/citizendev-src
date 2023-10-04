name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)

d = dict()
for line in fh:
    if line.startswith("From "):                
        time = line.strip().split(" ")                        
        hour = (time[6][0:2])        
        if hour not in d:
            d[hour] = 1
        else:
            d[hour] = d[hour] + 1

for k, v in sorted(d.items()):
    print(k, v)

fh.close()