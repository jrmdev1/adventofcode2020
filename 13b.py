#Advent of code 2020
# 08/13/21 day 13b
#import copy
import sys

filename = "data13_short2.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
#maxcolumns = len(a_list[0])
print(a_list)
print(f"maxrows={maxrows}")

buses = a_list[1].split(",")  #need the x's now....
lastBusIndex = len(buses)-1
print(f"{buses} lastBusIndex={lastBusIndex}")

# def findFactorOnOrAfter( timestamp, bus_int ):
#     mul = timestamp // bus_int
#     leaving = (mul+1) * bus_int  # bus after the timestamp
#     #remain = 
#     print(f"bus_int={bus_int}, timestamp={timestamp}, leaving={leaving}, mul={mul}")
#     return leaving, mul

# for each entry, find next factor, use current t for seed
#   increment t, check for factor, 
# if not factor, restart with new seed (?) on first entry
# if factor, increment t and try next one.
# if last bus, and did get a factor, then done 

done = False
first_bus_ts = 0
t = 1 # 1200001486 # 1202161486 #TODO: try precalc start number!
while not done:
    for bus in buses:
        #print(f"bus={bus}, index={buses.index(bus)}, t={t}")
        # if t > 1068788:
        #     print(f"ERROR, exceeded test value")
        #     done = True
        #     break
        if bus == "x":
            #print(f"x seen")
            t += 1
        else:
            remain = t % int(bus)
            if remain == 0:
                index = buses.index(bus)
                if index >= 2:  # reduce how often to print for speed.
                    print(f"FOUND A FACTOR! t={t}, index = {index}, bus={bus}")
                if index == 0:  # first
                    first_bus_ts = t
                if index == lastBusIndex:
                    done = True
                else:
                    #print(f"  factor but not last, continuing t={t}")
                    t += 1   # t must be 1 more than last bus factor
                    #TODO: see if way to increment MUCH more than 1 for this case to speed up!!!!
            else:
                #print(f"not a factor, t={t}, bus={bus}")
                t += 1 # inc time to keep searching, and break to skip back to starting bus
                #TODO: see if way to increment MUCH more than 1 for this case to speed up!!!!
                break

print(f"Finished! t={t}, >>>> first bus timestamp = {first_bus_ts} <<<<")

