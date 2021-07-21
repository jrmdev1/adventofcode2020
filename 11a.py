#Advent of code 2020
# 07/20/21 day 11a
#import re


filename = "data11_short.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
print(a_list)
print(f"maxrows={maxrows}, maxcolumns={len(a_list[0])}")

def checkSeat( char ):
    global a_list
    global maxrows
    global maxcolumns
    temp = 0

needExit = False
while not needExit:
    print(f"New Pass:")
    prev_list = a_list
    for r, row in enumerate(a_list):
        print(f"row: {row}")
        #row_id = 0
        for c, char in enumerate(row):
            if char == ".":   #floor, skip it
                continue
            elif char == "L":    # empty, check around it.
                x=0
            elif char == "#":    # occupied, check around it.
                x=0
            else:
                print(f"INVALID CHAR!")
                needExit = True
                break
        if needExit:
            break


