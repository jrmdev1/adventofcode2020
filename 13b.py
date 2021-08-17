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

#timestamp = int(a_list[0])
timestamp = 99999
#print(f"timestamp = {timestamp}")
#buses = a_list[1].replace(",x","").split(",")
buses = a_list[1].split(",")  #we need the x's now....
print(f"{buses}")
bus_t = []
for bus in buses:
    bus_t.append(int(0))

def findFactorOnOrAfter( timestamp, bus_int ):
    factor = timestamp // bus_int
    leaving = (factor+1) * bus_int  # bus after the timestamp
    return leaving, factor

# 13a: find the earliest bus you can take to the airport
lowest = sys.maxsize
#print(f"lowest={lowest}")
lowest_bus = 0
done = False
t = 0
while not done:
    bus_t = []
    for bus in buses:
        if bus == "x":
            print(f"x found")
            t += 1
            #continue
        else:
            leaving, factor = findFactorOnOrAfter( t, int(bus))
            t = leaving
            index = buses.index(bus)
            print(f"bus={bus}, index = {index} factor={factor}, leaving={leaving}")
        bus_t.append(t)
        
    start_t = bus_t[0]-1
    good = False
    for temp_t in bus_t:
        if temp_t != start_t + 1:
            good = False
            break
        else:
            good = True
    if good:
        done = True    

print(f"t={t}")
#print(f"lowest: lowest_bus={lowest_bus}, lowest={lowest}")
# wait_time = lowest - timestamp
# print(f"wait_time = {wait_time}, multiplied = {wait_time*lowest_bus}")

# x = timestamp // int(bus)
# leaving = (x+1) * int(bus)  # one bus after the timestamp
# print(f"bus={bus}, index = {buses.index(bus)} x={x}, leaving={leaving}")
# if leaving < lowest:
#     lowest = leaving
#     lowest_bus = int(bus)
#     #print(f"  {bus}, {leaving}, {lowest}")

# print(f"bus={bus}, index = {buses.index(bus)} x={x}, leaving={leaving}")
# if leaving < lowest:
#     lowest = leaving
#     lowest_bus = int(bus)
#     #print(f"  {bus}, {leaving}, {lowest}")
