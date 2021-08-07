#Advent of code 2020
# 08/06/21 day 12b
#import copy

filename = "data12_short.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
#maxcolumns = len(a_list[0])
print(a_list)
print(f"maxrows={maxrows}")

facing = 90   # 0 = N, 90 = E, 180 = S, 270 = W
ns = 0        # coordinates: N > 0, S < 0
ew = 0        #              E > 0, W < 0

ns_delta = {0:1, 90:0, 180:-1, 270:0}
ew_delta = {0:0, 90:1, 180:0, 270:-1}

for line in a_list:
    action = line[0]
    val = int(line[1:])
    #print(f" action = {action}, val = {val}")
    if   action == "N":
        ns += val
    elif action == "S":
        ns -= val
    elif action == "E":
        ew += val
    elif action == "W":
        ew -= val
    elif action == "L":
        facing -= val
        if facing < 0:
            facing += 360
    elif action == "R":
        facing += val
        if facing >= 360:
            facing -= 360
    elif action == "F":
        print(f"F act: facing={facing}, val={val}")
        ns += ns_delta[facing]*val
        ew += ew_delta[facing]*val
        print(f"new ns = {ns}, ew = {ew}")
    else:
        print(f"Syntax error: {line}")
        break
    print(f"{line}: facing = {facing}, ns = {ns}, ew = {ew}")

print(f"Final: Manhattan distance = {abs(ns) + abs(ew)}")