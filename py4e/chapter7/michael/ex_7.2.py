# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ") 
fh = open(fname)   

#intialising
count = 0
total_s_conf = 0
str_of_int = "X-DSPAM-Confidence:"

for line in fh:
    if not line.startswith(str_of_int):
        continue

    #increase running count
    count = count + 1
    
    #increase running sum
    ##finding float value
    strlength = len(str_of_int)
    spos = line.find(str_of_int)
    s_conf = float (line[spos + strlength:])
    ##sum of float values
    total_s_conf = total_s_conf + s_conf

avg_s_conf = total_s_conf/count
print("Average spam confidence:", avg_s_conf)
    