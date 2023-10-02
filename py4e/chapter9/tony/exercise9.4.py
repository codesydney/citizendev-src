fn = input("Enter file:")
if len(fn) < 1:
    fn = "mbox-short.txt"
fh = open(fn)


def process_lines(fh):
    counts = {}
    for line in fh:
        if not line.startswith("From "):
            continue
        email = line.split()[1]
        counts[email] = counts.get(email, 0) + 1
    return counts


def process_dict(dict):
    email = None
    count = 0
    for k, v in dict.items():
        if v > count:
            email = k
            count = v
    return [email, count]


r = process_dict(process_lines(fh))
print(r[0], r[1])
