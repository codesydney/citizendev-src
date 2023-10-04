# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
  fh = open(fname)
  ctr   = 0
  ave   = 0
  total = 0
  
  for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    index  = line.find(":")
    number = line[index+1:]
    total  = total + float(number)
    ctr    += 1    
  ave = total / ctr
  
  print('Average spam confidence:' , ave)
  fh.close()
except:
    print('file can not be open')
    quit()

