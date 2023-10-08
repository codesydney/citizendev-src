name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dic = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        x = line.split()
        hours = x[5][0:2]

        if hours not in dic:
            dic[hours] = 1
        else:
            dic[hours] = dic[hours] + 1


hourTuple = tuple(dic)
tupleHourSort = sorted(hourTuple)


for v in tupleHourSort:
    print(v,dic[v])