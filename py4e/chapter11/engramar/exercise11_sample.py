import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_42.txt"
fh = open(name)

nums = []
total = []
for line in fh:
   nums = re.findall("[0-9]+", line)
   if len(nums) > 0:
       total += [int(x) for x in nums]

print(len(total))
print(sum(total))