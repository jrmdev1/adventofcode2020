#Advent of code 2020
# 07/20/21 day 11a
import copy

filename = "data11.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
maxcolumns = len(a_list[0])
#print(a_list)
print(f"maxrows={maxrows}, maxcolumns={maxcolumns}")
#make 2d array
matrix = []
for i in range(maxrows):
    matrix.append( list(a_list[i]))
#print(f"2d:\n{matrix}")

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

# If a seat is empty (L) and 
# there are no occupied seats adjacent to it, the seat becomes occupied
def checkNoOccupiedSeatsAround( r, c ):
    global matrix
    #print(f"check around {r}, {c}")
    # CAREFUL, will skip rest of checks if one returns FALSE
    if not Occupied(r-1,c-1) and not Occupied(r-1,c) and not Occupied(r-1,c+1) and \
        not Occupied(r,c-1) and not Occupied(r,c+1) and \
        not Occupied(r+1,c-1) and not Occupied(r+1,c) and not Occupied(r+1,c+1):
        return True
    else:
        return False

# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, 
# the seat becomes empty (L)
# Otherwise, the seat's state does not change.
def check4orMoreOccupied( r, c ):
    global matrix
    count = 0
    if not Occupied(r,c):    # middle seat must be occupied!
        return False
    for ri in range(-1, 2):
        for ci in range(-1, 2):
            if Occupied(r + ri, c + ci):
                count += 1
                # middle seat must be occupied, so assume count of 5 or greater.
                if count >= 5:
                    #Can exit early, if already at count check.
                    return True
    return False
  
def countOccupied():
    global matrix
    cnt = 0
    for row in matrix:
        for char in row:
            if char == "#":
                cnt +=1
    return cnt
    
changedmatrix = copy.deepcopy(matrix)
#print(f"matrix={matrix}")
#print(f"changedmatrix={changedmatrix}")
needExit = False
passNum = 0
while not needExit:
#for j in range(0,2):    # run just once or twice for test.
    print(f"Pass #{passNum}:")
    passNum += 1
    for r, row in enumerate(matrix):
        print(f"row: {row}")
        #row_id = 0
        for c, char in enumerate(row):
            #print(f"c={c}, char={char}")
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
        cnt = countOccupied()
        print(f"Num occupied = {cnt}")
        needExit = True
    else:
        matrix = copy.deepcopy(changedmatrix)
        print(f"Copied matrix from changedmatrix")