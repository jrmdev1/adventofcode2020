#Advent of code 2020
# 07/9/21 day9 9b
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
        val = a_list[cnt-1]
        print(f"No sum found! cnt={cnt}, val={val}")
        break

print(f"val={val}")
val_int = int(val)

# part 2 (b)
cnt = 0
for entry in a_list:
    cnt += 1
    print(f"cnt={cnt}")
    y = cnt
    sum = 0
    found = False
    while True:
        sum += int(a_list[y-1])
        print(f"sum={sum}")
        if sum == val_int:
            print(f"sum found = {sum}, first cnt = {cnt}, last y = {y}, first={a_list[cnt-1]}")
            found = True
            break
        if sum > val_int:
            print(f"sum = {sum}, giving up on first {cnt}, since sum > {val_int}")
            found = False
            break
        y += 1

    if found == True:
        print(f"Done")
        break

smallest = float("inf")
largest = float(0)
for z in range(cnt, y+1):
    val_int = int(a_list[z-1])
    if val_int > largest:
        largest = val_int
    if val_int < smallest:
        smallest = val_int
print(f"smallest = {smallest}, largest = {largest}, sum = {smallest+largest}")