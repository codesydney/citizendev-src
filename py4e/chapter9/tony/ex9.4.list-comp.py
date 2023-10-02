fn = input("Enter file:")
if len(fn) < 1:
    fn = "mbox-short.txt"
fh = open(fn)


def process_file(fh):
    counts = {}
    for line in fh:
        if line.startswith("From "):
            email = line.split()[1]
            counts[email] = counts.get(email, 0) + 1
    return [[k, v] for k, v in counts.items() if v == max(counts.values())]


print(*process_file(fh)[0])
