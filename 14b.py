#Advent of code 2020
# 08/21/21 day 14b
#import copy
import sys
import re

# "{0:b}".format(10)
#f'0b{number:08b}'

filename = "data14_short.txt"
maxmemalloc = 65536
mem = [0] * maxmemalloc   #TODO: this will not be enough now due to X's
                          # 36-bit 68719476736 max

# address: 000000000000000000000000000000101010  (decimal 42)
# mask:    000000000000000000000000000000X1001X
# result:  000000000000000000000000000000X1101X

# If the bitmask bit is 0, the corresponding memory address bit is unchanged.
# If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
# If the bitmask bit is X, the corresponding memory address bit is floating.

def set_bit(x, pos):
    mask = 1 << pos
    return x | mask

def clear_bit(x, pos):
    mask = 1 << pos
    return x & ~mask

def read_bit(x, pos):
    mask = 1 << pos
    return (x & mask) >> pos

#def write_bit(x, pos):
    # n = read_bit(x, pos)
    # if n == 0:
    #     return clear_bit(x, pos)
    # else:
    #     return set_bit(x, pos)
def update_bit(num, pos, bit):
    mask = ~(1 << pos)
    return (num & mask) | (bit << pos)   
    # mask = 1 << pos
    # return (x & mask) >> pos

def applyMaskAndWrite(mask, address, val):
    # handles both 1 and 0 address bits now. 
    newaddress = address
    mask1 = mask.replace("X", "0")
    mask1_int = int(mask1, 2)
    print(f"mask1 binary = {mask1_int:b}")
    newaddress |= mask1_int 
    print(f"mask1={mask1}, mask1_int={mask1_int}, newaddress={newaddress}")

    # now if was X in mask, write 0 to newaddr for now (will change as cycled through later)
    mask0 =  mask.replace("1", "0")
    mask0 = mask0.replace("X", "1")
    mask0_int = int(mask0, 2)
    #print(f"mask0={mask0}, mask0_int={mask0_int}")
    newaddress &= ~mask0_int
    print(f"mask0={mask0}, mask0_int={mask0_int}, newaddress={newaddress}")
    print(f"newaddress={newaddress}, val={val}, bin={bin(newaddress)}")
    
    floating = []
    mask_reverse = mask[::-1]
    for ci,char in enumerate(mask_reverse):
        #print(f"char={char}")
        if char=="X":
            #print(f"ci={ci}")
            floating.append(ci)
    float_cnt = mask_reverse.count("X")

    print(f"float_cnt={float_cnt} floating={floating}")
    # incr = 0
    # for index in floating:
    #     # mem[newaddress] = val
    #     # newaddress |= 2**index
    #     # mem[newaddress] = val
    #     print(f"binary = {incr:036b}")
    #     incr += 1
    #     print(f"newaddress={newaddress},  val={val}")
    # for z in range(3):  # 4 = 100 binary
    #     print(f"z={z}, write={update_bit(5, z, 1)}")
    #     print(f"z={z}, read={read_bit(5, z)}")

    # increment mask integer number by 1 in outer loop. from 0 up to 2**num of X's
    # loop read bits spreading the bits using float index array over the X's in mask. up to float_cnt.
    # mask over the range of addresses and write to mem.
    incr = 0
    print(f"2**float_cnt={2**float_cnt}")
    print(f"mask={mask},  (newaddress={newaddress})")
    index = 0  # which float index to read from, then map to float bit to write to
    for incr in range(2**float_cnt):   # 4,
        modnewAddr = newaddress
        for index in range(float_cnt): # 2,
            bitval = read_bit(incr, index)
            print(f"incr={incr}, index={index}, bitval={bitval}")
            # use floating index for OUTPUT, (could use zip.)
            modnewAddr = update_bit(modnewAddr, floating[index], bitval)
        print(f"modnewAddr={modnewAddr}, val={val}, bin={bin(modnewAddr)}")
        mem[modnewAddr] = val
    return newaddress

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
print(a_list)
print(f"maxrows={maxrows}")

mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
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
        newaddr = applyMaskAndWrite(mask, address, val)

        if newaddr > max_mem:   #TODO: not enough anymore
            max_mem = newaddr
    else:
        print(f"ERROR {line}")

sum = 0
for i in range(maxmemalloc):  #TODO: this will not be enough now due to X's
    sum += mem[i]

print(f"max_mem = {max_mem}")
print(f"Sum = {sum}")