#Advent of code 2020
# 08/08/21 day 12b
#import copy

filename = "data12.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
#maxcolumns = len(a_list[0])
print(a_list)
print(f"maxrows={maxrows}")

ns = 0        # coordinates: N > 0, S < 0
ew = 0        #              E > 0, W < 0
wp_ns = 1     # waypoint (relative to ship, if ship moves, the waypoint moves with it.)
wp_ew = 10
err = False

def rotateRL(deg, wp_ns,wp_ew):
    # default assuming right, assume adjusted before calling if left.
    new_ns = new_ew  = 0
    my_err = False
    if deg == 90:
        new_ns = -wp_ew
        new_ew = wp_ns
    elif deg == 180:
        new_ns = -wp_ns
        new_ew = -wp_ew
    elif deg == 270:
        new_ns = wp_ew
        new_ew = -wp_ns
    else:
        print(f"invalid deg! = {deg}")
        my_err = True
    return new_ns, new_ew, my_err

for line in a_list:
    action = line[0]
    val = int(line[1:])
    #print(f" action = {action}, val = {val}")
    # move the waypoint "val" units, ship remains where it was.
    if   action == "N":
        wp_ns += val
    elif action == "S":
        wp_ns -= val
    elif action == "E":
        wp_ew += val
    elif action == "W":
        wp_ew -= val
    # rotate the WAYPOINT around the ship
    elif action == "L":
        if val == 90:
            val = 270
        elif val == 180:
            val = 180
        elif val == 270:
            val = 90
        else:
            print(f"error, bad left rotate val = {val}")
            err = True
        wp_ns, wp_ew, err = rotateRL( val, wp_ns, wp_ew)
    elif action == "R":
        wp_ns, wp_ew, err = rotateRL( val, wp_ns, wp_ew)
    # moves the ship to the waypoint "val" number of times.
    elif action == "F":
        print(f"  F act: val={val}")
        ns += wp_ns*val
        ew += wp_ew*val
        print(f"  wp_ns = {wp_ns}, wp_ew = {wp_ew}")
        print(f"  new ship ns = {ns}, ew = {ew}")
    else:
        print(f"Syntax error: {line}")
        err = True
        break
    if err:
        break
    print(f"{line}: ns={ns},ew={ew}, wp_ns={wp_ns},wp_ew={wp_ew}")

if err:
    print(f"INVALID RESULT, exit")
else:
    print(f"Final: Manhattan distance = {abs(ns) + abs(ew)}")