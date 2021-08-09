#Advent of code 2020
# 08/09/21 day 13a
#import copy

filename = "data13.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
#maxcolumns = len(a_list[0])
print(a_list)
print(f"maxrows={maxrows}")

timestamp = int(a_list[0])
print(f"timestamp = {timestamp}")
buses = a_list[1].replace(",x","").split(",")
print(f"{buses}")

lowest = 2008832
lowest_bus = 0
for bus in buses:
    x = timestamp // int(bus)
    leaving = (x+1) * int(bus)  # one bus after the timestamp
    print(f"bus={bus}, x={x}, leaving={leaving}")
    if leaving < lowest:
        lowest = leaving
        lowest_bus = int(bus)
        #print(f"  {bus}, {leaving}, {lowest}")

print(f"lowest: lowest_bus={lowest_bus}, lowest={lowest}")
wait_time = lowest - timestamp
print(f"wait_time = {wait_time}, multiplied = {wait_time*lowest_bus}")
