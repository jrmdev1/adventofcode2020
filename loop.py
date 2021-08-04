# loop neg from 2,2 to 0,0
# for r in range(2,0,-1):
#     print(f"r={-r} {-r + 1}")

# for r in [-1, -2, -3]:
#     print(f"r={r}")

# for r in range(2,-1,-1):
#     print(f"r={r} {-r + 1}")

# broken:
# it has end at 0 by default!
# it steps back ONLY to 0.
# should step back to negative numbers to really work.

# work on this part: need r,c =2,2, then need 1,1 and 0,0
# could try to step for full r,c passed in as parameters?
r = c = 2
ri = ci = -1
# r,c  = 2 -1 (ri) - 0 (arrow) (then step from arrow 0 up to r, and subtract)
#for arrow in range( 0, -1, -1): #TODO: broken, not neg, and stops at -1 (0) (but not supposed to be negative....) 
for arrow in range( 0, max(r,c)): 
    val = r+ri-arrow
    print(f"       r,c = {r},{c} ri,ci= {ri},{ci} arrow={arrow}, val = {val}")
    # if Occupied(r+ri+arrow, c+ci+arrow):
    #     count += 1
    #     break
print("")

r = c = 2
ri = 0 
ci = -1
#if ri == 0 and ci == -1:
# scan back to limit
# need for say 2,2:   r = same, c = 1, then 0.
# for arrow in range( c+ci, -1, -1): # neg step and stop at 0.
#     #val = r+ri+arrow
#     print(f"       r,c = {r},{c} ri,ci= {ri},{ci} arrow={arrow}, val = {val}")
#     # if Occupied(r+ri, arrow):
#     #     count += 1

maxrows = 10
maxcolumns = 10
ri = 0
ci = 1
for arrow in range( c+ci, maxcolumns): # 
    print(f"       r,c = {r},{c} ri,ci= {ri},{ci} arrow={arrow}")
    #if Occupied(r+ri, arrow):

print("")

r = c = 2
# ri = -1
# ci = 0
#if ri == -1 and ci == 0:
# for arrow in range( r+ri, -1, -1): # 
#     print(f"       r,c = {r},{c} ri,ci= {ri},{ci} arrow={arrow}, no val")
#     #if Occupied(arrow, c+ci):

# expect: rparm,cparm to be 1,3 0,4
ri = -1
ci = 1
for arrow in range( 0, max(maxrows,maxcolumns)): # 
    rparm = r+ri-arrow
    cparm = c+ci+arrow
    # if Occupied(r+ri-arrow, c+ci+arrow):
    print(f"       r,c = {r},{c} ri,ci= {ri},{ci} arrow={arrow}, rparm={rparm}, cparm={cparm}")

print("")

# expect: rparm,cparm to be 3,1 4,0
ri = 1
ci = -1
for arrow in range( 0, max(maxrows,maxcolumns)): # 
    rparm = r+ri+arrow
    cparm = c+ci-arrow
#     #if Occupied(r+ri+arrow, c+ci-arrow):
    print(f"       r,c = {r},{c} ri,ci= {ri},{ci} arrow={arrow}, rparm={rparm}, cparm={cparm}")
