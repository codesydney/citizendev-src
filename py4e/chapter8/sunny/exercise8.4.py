fname = input("Enter file name: ")
fh = open(fname)

words_list = list()

for line in fh:
    words_in_line = line.rstrip().split(" ")
    for word in words_in_line:
        if word not in words_list:
            words_list.append(word)
            print(words_list)

fh.close()
words_list.sort()
print(words_list)
