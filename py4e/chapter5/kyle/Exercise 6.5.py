text = "X-DSPAM-Confidence:    0.8475"

start = text.find('.')

extract = text[start-2:start+5]


print(float(extract))
