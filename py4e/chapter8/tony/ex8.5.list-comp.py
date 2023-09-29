fh = open("mbox-short.txt")
emails = [line.split()[1] for line in fh if line.startswith("From ")]
fh.close()
print("\n".join(emails))
print(f"There were {len(emails)} lines in the file with From as the first word")
