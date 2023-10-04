fn = input("Enter file:")
if len(fn) < 1:
    fn = "mbox-short.txt"
fh = open(fn)

counts = {}

for line in fh:
    if line.startswith("From "):
        hour = (line.split()[5]).split(":")[0]
        counts[hour] = counts.get(hour, 0) + 1

for k, v in sorted(counts.items()):
    print(k, v)
