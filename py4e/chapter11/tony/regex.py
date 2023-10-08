import re

fn = input("Enter file:")
if len(fn) < 1:
    fn = "regex_sum_1890739.txt"
fh = open(fn)

# nums = []
# for line in fh:
#    s_nums = re.findall("[0-9]+", line)
#    if len(s_nums) == 0:
#        continue
#    nums += [int(x) for x in s_nums]
# print(sum(nums))

print(sum([int(x) for x in re.findall("[0-9]+", fh.read())]))
