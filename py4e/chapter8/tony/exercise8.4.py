fh = open("romeo.txt")
lst = list()

for line in fh:
    for word in line.split():
        if word in lst:
            continue
        lst.append(word)

fh.close()
lst.sort()
print(lst)
