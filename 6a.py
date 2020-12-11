#Advent of code
# 12/11/2020 day6 6a
filename = "data5.txt"
file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxindex = len(a_list)
#print(a_list)
print(f"maxindex={maxindex}, maxcolumns={len(a_list[0])}")

