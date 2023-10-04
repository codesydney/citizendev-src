fn = input("Enter file:")
if len(fn) < 1:
    fn = "mbox-short.txt"
fh = open(fn)

counts = {}

for line in fh:
    if line.startswith("From "):
        email = line.split()[1]
        counts[email] = counts.get(email, 0) + 1

r = [[k, v] for k, v in counts.items() if v == max(counts.values())]
print(*r[0])
