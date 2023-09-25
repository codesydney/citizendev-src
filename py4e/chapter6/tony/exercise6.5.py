text = "X-DSPAM-Confidence:    0.8475"

index = text.find(":") + 1
print(float(text[index:]))

