#Advent of code
# 07/7/21 day9 9a
#import re

filename = "data9.txt"
preamble_len = 25       #TODO: Set preamble length!

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxindex = len(a_list)
#print(a_list)
print(f"maxindex={maxindex}, maxcolumns={len(a_list[0])}")

cnt = 0
for entry in a_list:
    cnt += 1
    print(f"cnt={cnt}")
    if cnt <= preamble_len:
        continue
    start = cnt - preamble_len
    found = False
    for y in range(start, start+preamble_len ):
        for z in range( y+1, cnt ):
            print(f"cnt={cnt}, y={y}, z={z}")
            sum = int(a_list[y-1]) + int(a_list[z-1])
            if int(a_list[cnt-1]) == sum:
                print(f"cnt={cnt}, good sum found={sum}")
                found = True
                break
        if found:
            break
    if not found:
        print(f"No sum found! cnt={cnt}, val={a_list[cnt-1]}")
        break

