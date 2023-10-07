file_name = input("Enter file:")
if len(file_name) < 1:
    file_name = "mbox-short.txt"

email_dictionary = dict()

max_count = -1
max_email = ""

with open(file_name) as handle:
    for line in handle:
        if line.startswith("From:"):
            email = line.split()[1]
            email_occurences = email_dictionary.get(email, 0)
            email_occurences = email_occurences + 1
            if email_occurences > max_count:
                max_count = email_occurences
                max_email = email
            email_dictionary[email] = email_occurences

print(f"{max_email} {max_count}")
