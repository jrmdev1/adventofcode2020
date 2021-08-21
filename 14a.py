#Advent of code 2020
# 08/21/21 day 14a
#import copy
import sys
import re

filename = "data14_short.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
#maxcolumns = len(a_list[0])
print(a_list)
print(f"maxrows={maxrows}")

# 36 bits
# mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11

for line in a_list:
    if line[:7] == "mask = ":
        print(f"mask line: {line}")
        temp = line.split(" = ")
        mask = temp[1]
        print(f"found mask = {mask}")
    elif line[:3] == "mem":
        print(f"mem line: {line}")
        temp = line.split(" = ")
        index_list_str = re.findall(r"\d+", temp[0])
        index = int(index_list_str[0])
        val = int(temp[1])
        print(f"index = {index} val={val}")
    else:
        print(f"ERROR {line}")

