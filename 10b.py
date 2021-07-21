#Advent of code 2020
# 07/17/21 day 10b
#import re

filename = "data10.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxindex = len(a_list)
#print(a_list)
print(f"maxindex={maxindex}, maxcolumns={len(a_list[0])}")

num_list = list(map(int, a_list))
num_max = max(num_list)
num_min = min(num_list)
print(f"{num_list}, max={num_max}, min={num_min}")

sorted_list = sorted(num_list)
print(f"{sorted_list}")

diff1 = 0
diff3 = 0
prev = 0
for num in sorted_list:
    if num - prev == 1:
        diff1 += 1
    if num - prev == 3:
        diff3 += 1
    prev = num

# for final adapter.
diff3 += 1

print(f"diff1={diff1}, diff3={diff3}, multiplied={diff1*diff3}")
