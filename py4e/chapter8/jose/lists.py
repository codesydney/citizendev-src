abc = "With three words"

#convert this string into array list
#split
stuff = abc.split()
print(stuff)
print(stuff[:1] )# slice

fhand =  open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])

a = [1,2,3]
b = [4,5,6]
#sliced
print(a[:2])


#empty list - like array
stuff = list()
def addTomyList(item):
    global stuff
    while True:
        answerItem = input('Do you want to add items to the list? (yes/no)\n')
        if answerItem.lower() == "yes" or answerItem.lower() == 'y':
            new_item = input('Enter the item you want to add to the list:\n')
            stuff.append(new_item)
           # print(stuff)
        else:
            # return False
             break
    stuff.append(item)
    print(stuff)
    print('this list has all this items' , len(stuff))
       
    

addTomyList('arrays')

programminglist = ['python', 'linux', 'php', 'javaacript', 'css', 'html', 'arrays']
stuff2 = list()

for item in programminglist:
    #print(item)
    if item.lower() == 'python':
        print('best languages' , item)
    else:
       print(item)

numlist = list()
while True:
    inp = input('enter  a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist) #sum suma los elementos
print('Average',average)