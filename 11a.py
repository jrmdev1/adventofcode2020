#Advent of code 2020
# 07/20/21 day 11a
#import re

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

filename = "data11_short.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
print(a_list)
print(f"maxrows={maxrows}, maxcolumns={len(a_list[0])}")

def checkNoOccupiedSeatsAround( r, c ):
    global a_list
    global maxrows
    global maxcolumns
    #TODO: complete!
    
    return True
    
def check4OrMoreOccupied( r, c ):
    global a_list
    global maxrows
    global maxcolumns
    #TODO: complete!
        
    return False


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
                if checkNoOccupiedSeatsAround( r, c ):
                    a_list[r,c] = "#"
            elif char == "#":    # occupied, check around it.
                if check4OrMoreOccupied( r, c ):
                    a_list[r,c] = "L"
            else:
                print(f"INVALID CHAR!")
                needExit = True
                break
        if needExit:
            break


