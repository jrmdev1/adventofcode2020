#Advent of code 2020
# 07/22/21 day 11b
import copy

filename = "data11_short.txt"

r_check = 3
c_check = 9

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

def Empty( r, c ):
    global matrix
    global maxrows
    global maxcolumns
    #print(f"r={r},c={c}")
    if r < 0 or r >= maxrows or c < 0 or c >= maxcolumns:
        return True  # if exceeds bounds, then EMPTY.
    if matrix[r][c] == "L": 
        return True
    else:
        return False

# If a seat is empty (L) and 
# there are no occupied seats adjacent to it, the seat becomes occupied
def checkNoOccupiedSeatsAround( r, c ):
    global matrix
    global maxrows
    global maxcolumns
    #print(f"check no occ around {r}, {c}")
    # will skip rest of checks if one returns FALSE
    for ri in range(-1,2):
        for ci in range(-1,2):
            if ri==0 and ci==0:
                continue
            # -1,-1 -1,0 -1,1 0,-1 0,0 0,1 1,-1 1,0 1,1
            if ri == 0 and ci == -1:
                # scan back to limit
                for c_arrow in range( c+ci, -1, -1): # neg step and stop at 0.
                    if Occupied(r+ri, c_arrow):
                        return False
                    elif Empty(r+ri, c_arrow):
                        break
            elif ri == 0 and ci == 1:
                for c_arrow in range( c+ci, maxcolumns): # 
                    if Occupied(r+ri, c_arrow):
                        return False
                    elif Empty(r+ri, c_arrow):
                        break
            elif ri == -1 and ci == 0:
                for r_arrow in range( r+ri, -1, -1): # 
                    if Occupied(r_arrow, c+ci):
                        return False
                    elif Empty(r_arrow, c+ci):
                        break
            elif ri == 1 and ci == 0:
                for r_arrow in range( r+ri, maxrows): # 
                    if Occupied(r_arrow, c+ci):
                        return False
                    elif Empty(r_arrow, c+ci):
                        break
            elif ri == 1 and ci == 1:
                for offset in range( 0, max(maxrows,maxcolumns) ): # 
                    if Occupied(r+ri+offset, c+ci+offset):
                        return False
                    elif Empty(r+ri+offset, c+ci+offset):
                        break
            elif ri == -1 and ci == -1:
                for offset in range( 0, -1, -1): # 
                    if Occupied(r+ri+offset, c+ci+offset):
                        return False
                    elif Empty(r+ri+offset, c+ci+offset):
                        break
            elif ri == -1 and ci == 1:
                for offset in range( 0, max(maxrows,maxcolumns)): # 
                    if Occupied(r+ri-offset, c+ci+offset):
                        return False
                    elif Empty(r+ri-offset, c+ci+offset):
                        break
            elif ri == 1 and ci == -1:
                for offset in range( 0, max(maxrows,maxcolumns)): # 
                    if Occupied(r+ri+offset, c+ci-offset):
                        return False
                    elif Empty(r+ri+offset, c+ci-offset):
                        break
    return True

# If a seat is occupied (#) and five or more seats adjacent to it are also occupied, 
# the seat becomes empty (L)
# Otherwise, the seat's state does not change.
def check5orMoreOccupied( r, c ):
    global matrix
    global maxrows
    global maxcolumns
    count = 0
    if r==r_check and c==c_check:
        print(f"check 5+ occ around {r}, {c}")
    if not Occupied(r,c):    # middle seat must be occupied!
        return False
    for ri in range(-1, 2):
        for ci in range(-1, 2):
            if ri==0 and ci==0:
                continue
            # -1,-1 -1,0 -1,1 0,-1 0,0 0,1 1,-1 1,0 1,1
            if ri == 0 and ci == -1:
                # scan back to limit
                for c_arrow in range( c+ci, -1, -1): # neg step and stop at 0.
                    if Occupied(r+ri, c_arrow):
                        count += 1
                        break
            elif ri == 0 and ci == 1:
                for c_arrow in range( c+ci, maxcolumns): # 
                    if Occupied(r+ri, c_arrow):
                        count += 1
                        break
            elif ri == -1 and ci == 0:
                for r_arrow in range( r+ri, -1, -1): # 
                    if Occupied(r_arrow, c+ci):
                        count += 1
                        break
            elif ri == 1 and ci == 0:
                for r_arrow in range( r+ri, maxrows): # 
                    if Occupied(r_arrow, c+ci):
                        count += 1
                        break
            elif ri == 1 and ci == 1:
                for offset in range( 0, max(maxrows,maxcolumns) ): # 
                    if Occupied(r+ri+offset, c+ci+offset):
                        count += 1
                        break
            elif ri == -1 and ci == -1:
                for offset in range( 0, -1, -1): # 
                    if Occupied(r+ri+offset, c+ci+offset):
                        count += 1
                        break
            elif ri == -1 and ci == 1:
                for offset in range( 0, max(maxrows,maxcolumns)): # 
                    if Occupied(r+ri-offset, c+ci+offset):
                        count += 1
                        break
            elif ri == 1 and ci == -1:
                for offset in range( 0, max(maxrows,maxcolumns)): # 
                    if Occupied(r+ri+offset, c+ci-offset):
                        count += 1
                        break
            #print(f"check 5+ occ around {r}, {c}, occ count = {count}")
            if r==r_check and c==c_check:
                print(f"rc {r},{c} ri={ri},ci={ci} count = {count}")
            if count >= 5:
                if r==r_check and c==c_check:
                    print(f"   Change {r},{c} # to L, count = {count}")
                return True
            
            #### TODO: OLD CODE!!!!! REMOVE!!!
            # if Occupied(r + ri, c + ci):
            #     count += 1
            #     # middle seat must be occupied, so assume count of 5 or greater.
            #     if count >= 5:
            #         #Can exit early, if already at count check.
            #         return True
    return False
  
def countOccupied():
    global matrix
    cnt = 0
    for row in matrix:
        for char in row:
            if char == "#":
                cnt +=1
    return cnt

#def checkAndPrintChangedWatch()

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
        str_row = "".join(row)
        print(f"row: {str_row}")
        #row_id = 0
        for c, char in enumerate(row):
            #print(f"c={c}, char={char}")
            if char == ".":   #floor, skip it
                continue
            elif char == "L":    # empty, check around it.
                if checkNoOccupiedSeatsAround( r, c ):
                    changedmatrix[r][c] = "#"
                    if r==r_check and c==c_check:
                        print(f"    rc {r},{c} changed to #")
            elif char == "#":    # occupied, check around it.
                if check5orMoreOccupied( r, c ):
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