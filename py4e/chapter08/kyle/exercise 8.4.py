fname = input("Enter file name: ")
fh = open(fname)
lst = list()  

for line in fh:
    info = line.split()  
    for word in info:
        if word not in lst:  
            lst.append(word)  

lst.sort()

print(lst)
