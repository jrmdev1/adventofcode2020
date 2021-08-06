#Advent of code 2020
# 08/05/21 day 12a
import copy

filename = "data12_short.txt"

# r_check = -1
# c_check = -1

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
maxcolumns = len(a_list[0])
print(a_list)
print(f"maxrows={maxrows}, maxcolumns={maxcolumns}")
#make 2d array
# matrix = []
# for i in range(maxrows):
#     matrix.append( list(a_list[i]))
#print(f"2d:\n{matrix}")

