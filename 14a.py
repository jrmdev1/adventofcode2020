#Advent of code 2020
# 08/21/21 day 14a
#import copy
import sys
import re

# "{0:b}".format(10)
#f'0b{number:08b}'

def applyMask(mask, val):
    newval = val
    mask1 = mask.replace("X", "0")
    mask1_int = int(mask1, 2)
    #print(f"mask1 binary = {mask1_int:b}")
    newval |= mask1_int 
    #print(f"mask1={mask1}, mask1_int={mask1_int}, newval={newval}")

    mask0 = mask.replace("X", "1")
    mask0_int = ~(int(mask0, 2))
    #print(f"mask0 binary = {mask0_int:b}")
    #print(f"mask0={mask0}, mask0_int={mask0_int}, newval={newval}")
    newval &= ~mask0_int

    print(f"mask={mask}, val={val}, newval={newval}")
    return newval

filename = "data14.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
#maxcolumns = len(a_list[0])
print(a_list)
print(f"maxrows={maxrows}")

# 36 bits. MSbit on left, LSbit on right
# mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11

mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

mem = [0] * 65535
max_mem = 0

for line in a_list:
    if line[:7] == "mask = ":
        #print(f"mask line: {line}")
        temp = line.split(" = ")
        mask = temp[1]
        print(f"found mask = {mask}")       
    elif line[:3] == "mem":
        #print(f"mem line: {line}")
        temp = line.split(" = ")
        index_list_str = re.findall(r"\d+", temp[0])
        index = int(index_list_str[0])
        val = int(temp[1])
        print(f"index = {index} val={val}")
        newval = applyMask(mask, val)
        
        mem[index] = newval

        if index > max_mem:
            max_mem = index
    else:
        print(f"ERROR {line}")

sum = 0
for i in range(65535):
    sum += mem[i]

print(f"max_mem = {max_mem}")
print(f"Sum = {sum}")