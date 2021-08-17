#Advent of code 2020
# 08/13/21 day 13b
#import copy
import sys

filename = "data13_short.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
#maxcolumns = len(a_list[0])
print(a_list)
print(f"maxrows={maxrows}")

buses = a_list[1].split(",")  #we need the x's now....
lastBusIndex = len(buses)-1
print(f"{buses} lastBusIndex={lastBusIndex}")

def findFactorOnOrAfter( timestamp, bus_int ):
    factor = timestamp // bus_int
    leaving = (factor+1) * bus_int  # bus after the timestamp
    print(f"bus_int={bus_int}, timestamp={timestamp}, leaving={leaving}, factor={factor}")
    return leaving, factor

# for each entry, find next factor, use current t for seed
#   increment t, check for factor, 
# if not factor, restart with new seed (?) on first entry
# if factor, increment t and try next one.
# if last bus, and did get a factor, then done 

done = False
t = 0
while not done:
    for bus in buses:
        print(f"bus={bus}, index={buses.index(bus)}, t={t}")
        if t > 1068781:
            print(f"ERROR, exceeded test value")
            done = True
            break
        if bus == "x":
            print(f"x seen")
            t += 1
        else:
            leaving, factor = findFactorOnOrAfter( t, int(bus))
            if t == factor: # TODO: this may be problem, in that may not equal after?
                if buses.index(bus) == lastBusIndex:
                    done = True
                else:
                    print(f"restarting first bus using t={t}")
                    t = leaving + 1
                    break
            else:
                print(f"not a factor, t={t}, bus={bus}")
            t = leaving + 1

print(f"t={t}")

# print(f"bus={bus}, index = {buses.index(bus)} x={x}, leaving={leaving}")
# if leaving < lowest:
#     lowest = leaving
#     lowest_bus = int(bus)
#     #print(f"  {bus}, {leaving}, {lowest}")

    # bus_t = []
    # for bus in buses:
    #     if bus == "x":
    #         print(f"x found")
    #         t += 1
    #         #continue
    #     else:
    #         leaving, factor = findFactorOnOrAfter( t, int(bus))
    #         t = leaving
    #         index = buses.index(bus)
    #         print(f"bus={bus}, index = {index} factor={factor}, leaving={leaving}")
    #     bus_t.append(t)
        
    # start_t = bus_t[0]-1
    # good = False
    # for temp_t in bus_t:
    #     if temp_t != start_t + 1:
    #         good = False
    #         break
    #     else:
    #         good = True
