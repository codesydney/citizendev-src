text = "X-DSPAM-Confidence:    0.8475"
atpos = text.find(':')
num = text[atpos+1:len(text)]
print (float(num))