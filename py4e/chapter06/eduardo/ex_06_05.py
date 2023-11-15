# Reference text
text = "X-DSPAM-Confidence:    0.8475"

# Find the colon character in the text
posFirstNumber = text.find(':')

# Slice, parse to float and print the number from the reference text
textSlice = text[posFirstNumber+1:]
number = float(textSlice)
print(number)



