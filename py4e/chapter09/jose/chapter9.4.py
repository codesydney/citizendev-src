name = input("Enter file:")
if len(name) < 1:
   name = "mbox-short.txt"
handle = open(name)

diccionario = dict()
for line in handle:
    if line.startswith('From '):
        email = line.rstrip().split(' ')
        if email[1] not in diccionario:
            diccionario[email[1]] = 1
        else:
            diccionario[email[1]] =  diccionario[email[1]] + 1

maxCount       = 0
commonEmail    = None

for correo, key in diccionario.items():
  
  #print(correo, key)
  if key > maxCount:
      maxCount = key
      commonEmail = correo
print(commonEmail,maxCount)
# print(len(diccionario))