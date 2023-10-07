file_name = input("Enter file name:")
if len(file_name) < 1:
    file_name = "mbox-short.txt"
file_handle = open(file_name)

hour_dictionary = dict()

with open(file_name) as file_handle:
    for line in file_handle:
        if line.startswith("From "):
            line_parts = line.rstrip().split()
            hour = line_parts[-2].split(":")[0]
            hour_occurences = hour_dictionary.get(hour, 0)
            hour_occurences = hour_occurences + 1
            hour_dictionary[hour] = hour_occurences

hour_list = list(hour_dictionary.items())
hour_list.sort()

for hour, freq in hour_list:
    print(hour, freq)
        