#Advent of code
# 12/7/2020 day3 3a

filename = "data3.txt"
file = open(filename)
filestr = file.read()
a_str = filestr.split("\n")
a = a_str
maxindex = len(a)
print(a)
print(f"maxindex={maxindex}, maxcolumns={len(a[0])}")

line = 0
col = 0
maxcol = len(a[0])  # 11 in short data, longer in real file
maxline = maxindex - 1   #10 in short data file, longer in real file
trees = 0

while True:
    col = col + 3
    if col >= maxcol:
        col = col - maxcol
    line = line + 1
    if line > maxline:
        print(f"total trees = {trees}")
        break
    current = a[line]
    print (f"col={col}, line={line}, linelen={len(current)}")
    val = current[col]
    if val == "#":
        trees = trees + 1
    print (f"val={val}, trees = {trees}")

exit()