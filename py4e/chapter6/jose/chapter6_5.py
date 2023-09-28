text = "X-DSPAM-Confidence:    0.8475"
number  =  text.find(':')+1
parseResultado = float(text[number:30])
print(parseResultado)
