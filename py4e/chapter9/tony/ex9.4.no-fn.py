fn = input("Enter file:")
if len(fn) < 1:
    fn = "mbox-short.txt"
fh = open(fn)

counts = {}
count = 0
email = None

for line in fh:
    if line.startswith("From "):
        email = line.split()[1]
        counts[email] = counts.get(email, 0) + 1

for k, v in counts.items():
    if v > count:
        email = k
        count = v

print(email, count)
