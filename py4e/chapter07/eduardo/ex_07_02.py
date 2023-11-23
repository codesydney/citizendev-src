fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened:',fname)
    quit()

count = 0
total_dspam_confidence = 0

for line in fh:
    # Confidence rate in each line
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    # Count of lines where X-DSPAM confidence data was found     
    count += 1

    # Find the colon character in the text
    posFirstNumber = line.find(':')

    # Slice, parse to float and add to the total confidence
    textSlice = line[posFirstNumber+1:]
    number = float(textSlice)
    total_dspam_confidence += number
    
# Calculate and print the average spam confidence
average_confidence = total_dspam_confidence / count
print("Average spam confidence:", average_confidence)

