#Advent of code 2020
# 07/20/21 day 11a
filename = "data11_short.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
maxcolumns = len(a_list[0])
print(a_list)
print(f"maxrows={maxrows}, maxcolumns={maxcolumns}")
#make 2d array
matrix = []
for i in range(maxrows):
    matrix.append( list(a_list[i]))
print(f"2d:\n{matrix}")

# If a seat is empty (L) and 
# there are no occupied seats adjacent to it, the seat becomes occupied
def notOccupied( r, c ):
    global matrix
    global maxrows
    global maxcolumns
    print(f"r={r},c={c}")
    if (r < 0) or (r >= maxrows) or (c < 0) or (c >= maxcolumns):
        return True  # skip it, it is okay, even if bounds exceeded.
    print(f"val={matrix[r][c]}")
    if matrix[r][c] == "#":  # can be either empty, or floor.
        return False
    return True

def checkNoOccupiedSeatsAround( r, c ):
    global matrix
    global maxrows
    global maxcolumns
    print(f"check {r}, {c}")
    if notOccupied(r-1,c-1) and notOccupied(r-1,c) and notOccupied(r-1,c+1) and \
        notOccupied(r,c-1) and notOccupied(r,c+1) and \
        notOccupied(r+1,c-1) and notOccupied(r+1,c) and notOccupied(r+1,c+1):
        return True
    else:
        return False

# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, 
# the seat becomes empty (L)
# Otherwise, the seat's state does not change.
def Occupied( r, c ):
    global matrix
    global maxrows
    global maxcolumns
    #print(f"r={r},c={c}")
    if r < 0 or r >= maxrows or c < 0 or c >= maxcolumns:
        return False  # if exceeds bounds, then NOT occupied.
    if matrix[r][c] == "#": 
        return True
    else:
        return False # cannot be floor, or empty

def check4orMoreOccupied( r, c ):
    global matrix
    global maxrows
    global maxcolumns
    count = 0
    for ri in range(-1, 2):
        for ci in range(-1, 2):
            if Occupied(r + ri, c + ci):
                count += 1
    # middle seat must be occupied, so assume count of 5 or greater.
    if Occupied(r,c) and count >= 5:
        return True
    else:
        return False

changedmatrix = matrix
needExit = False
passNum = 0
#while not needExit:
for j in range(0,1):    # run just once or twice for test.
    print(f"New Pass #{passNum}:")
    passNum += 1
    #prev_list = matrix    #TODO: NEED TO RUN ON THE PREVIOUS MATRIX!
    for r, row in enumerate(matrix):
        print(f"row: {row}")
        #row_id = 0
        for c, char in enumerate(row):
            print(f"c={c}, char={char}")
            if char == ".":   #floor, skip it
                continue
            elif char == "L":    # empty, check around it.
                if checkNoOccupiedSeatsAround( r, c ):
                    changedmatrix[r][c] = "#"
            elif char == "#":    # occupied, check around it.
                if check4orMoreOccupied( r, c ):
                    changedmatrix[r][c] = "L"
            else:
                print(f"INVALID CHAR!")
                needExit = True
                break
        if needExit:
            break
    
    if matrix == changedmatrix:
        print(f"NO Changes. Pass complete!")
        print(f"{matrix}")
        needExit = True
    #else:
    matrix = changedmatrix
    print(f"Copied matrix from changedmatrix")