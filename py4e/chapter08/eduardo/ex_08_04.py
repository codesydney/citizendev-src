# prompt user to input the file name 
fname = input("Enter file name: ")

# try-except block to catch any user input errors
try:
    fh = open(fname)
except:
    print('File cannot be opened:',fname)
    quit()

# empty list to append distinct words from the file read
lst = list()

# for each line, split words by empty spaces, and adds distinct words to the list
for line in fh:
    sline = line.split()
    for each in sline:
        if each not in lst:
            lst.append(each)

# sort the list and prints list
lst.sort()
print(lst)
