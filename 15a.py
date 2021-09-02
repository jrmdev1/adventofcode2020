#Advent of code 2020
# 09/01/21 day 15a
# import sys
# import re

filename = "data15_short.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxrows = len(a_list)
print(a_list)
print(f"maxrows={maxrows}")
b_list = a_list[0].split(",")
print(b_list)

