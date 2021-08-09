#Advent of code 2020
# 08/09/21 day 13a
#import copy

filename = "data13_short.txt"

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

for bus in buses:
    print(f"bus={bus}")



print(f" ")