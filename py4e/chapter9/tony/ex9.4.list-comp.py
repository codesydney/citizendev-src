fn = input("Enter file:")
if len(fn) < 1:
    fn = "mbox-short.txt"
fh = open(fn)


def process_lines(fh):
    counts = {}
    for line in fh:
        if line.startswith("From "):
            email = line.split()[1]
            counts[email] = counts.get(email, 0) + 1
    return counts


def process_dict(d):
    return [[k, v] for k, v in d.items() if v == max(d.values())]


r = process_dict(process_lines(fh))
print(*r[0])
