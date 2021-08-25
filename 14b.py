#Advent of code 2020
# 08/21/21 day 14a
#import copy
import sys
import re

filename = "data14_short2.txt"

# "{0:b}".format(10)
#f'0b{number:08b}'

# If the bitmask bit is 0, the corresponding memory address bit is unchanged.
# If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
# If the bitmask bit is X, the corresponding memory address bit is floating.
def applyMaskAndWrite(mask, address, val):
    # OK, and handles both 1 and 0 address bits now.
    newaddress = address
    mask1 = mask.replace("X", "0")
    mask1_int = int(mask1, 2)
    #print(f"mask1 binary = {mask1_int:b}")
    newaddress |= mask1_int 
    #print(f"mask1={mask1}, mask1_int={mask1_int}, newaddress={newaddress}")

    #TODO: change to handle X now?
    # LOOP through ALL X combinations and write
    #mask0 = mask.replace("X", "1")
    #mask0_int = ~(int(mask0, 2))
    #print(f"mask0 binary = {mask0_int:b}")
    #print(f"mask0={mask0}, mask0_int={mask0_int}, newaddress={newaddress}")
    
    #newaddress &= ~mask0_int
    # loop!!!!
    mem[newaddress] = val  #TODO: only writing one val for now

    print(f"mask={mask}, address={address}, newaddress={newaddress},  val={val}")
    return newaddress

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

mem = [0] * 65535   #TODO: this will not be enough now due to X's
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
        address_list_str = re.findall(r"\d+", temp[0])
        address = int(address_list_str[0])
        val = int(temp[1])
        print(f"address = {address} val={val}")
        #newaddress = applyMask(mask, address)
        newaddr = applyMaskAndWrite(mask, address, val)
        
        #mem[address] = newaddress
        #mem[newaddr] = val  #TODO: DONT write here now...

        if newaddr > max_mem:
            max_mem = newaddr
    else:
        print(f"ERROR {line}")

sum = 0
for i in range(65535):  #TODO: this will not be enough now due to X's
    sum += mem[i]

print(f"max_mem = {max_mem}")
print(f"Sum = {sum}")