#Advent of code 2020
# 08/08/21 day 12b
#import copy

filename = "data12_short.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
#maxcolumns = len(a_list[0])
print(a_list)
print(f"maxrows={maxrows}")

ship_facing = 90   # 0 = N, 90 = E, 180 = S, 270 = W
ns = 0        # coordinates: N > 0, S < 0
ew = 0        #              E > 0, W < 0
wp_ns = 1     # waypoint (relative to ship, if ship moves, the waypoint moves with it.)
wp_ew = 10

ns_delta = {0:1, 90:0, 180:-1, 270:0}
ew_delta = {0:0, 90:1, 180:0, 270:-1}

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
        wp_facing -= val
        if wp_facing < 0:
            wp_facing += 360
    elif action == "R":
        wp_facing += val
        if wp_facing >= 360:
            wp_facing -= 360
    # moves the ship to the waypoint "val" number of times.
    elif action == "F":
        print(f"  F act: val={val}")
        #ns += ns_delta[ship_facing]*val
        #ew += ew_delta[ship_facing]*val
        wp_ns_diff = wp_ns - ns  #TODO: not right, remember it is relative to ship! (see print output)
        wp_ew_diff = wp_ew - ew
        ns += wp_ns_diff*val
        ew += wp_ew_diff*val
        print(f"  wp_ns_diff = {wp_ns_diff}, wp_ew_diff = {wp_ew_diff}")
        print(f"  new ship ns = {ns}, ew = {ew}")
    else:
        print(f"Syntax error: {line}")
        break
    print(f"{line}: ship_facing = {ship_facing}, ns={ns},ew={ew}, wp_ns={wp_ns},wp_ew={wp_ew}")

print(f"Final: Manhattan distance = {abs(ns) + abs(ew)}")