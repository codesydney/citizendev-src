text = "X-DSPAM-Confidence:    0.8475"

blankspace = text.find(' ')
end_string = text[blankspace:]
number = end_string.lstrip()
number = float(number) 
print(number)