fname = input("Enter file name: ")
try:
    fh = open(fname)
    list = list()
    for line in fh:
        wordlist = line.rstrip().split()
        for word in wordlist:
            if word not in list:
                list.append(word)
except:
  print('something went wrong')
list.sort()
print(list)