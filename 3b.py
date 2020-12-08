#Advent of code
# 12/7/2020 day3 3b

filename = "data3.txt"
file = open(filename)
filestr = file.read()
a_str = filestr.split("\n")
a = a_str
maxindex = len(a)
print(a)
print(f"maxindex={maxindex}, maxcolumns={len(a[0])}")

maxcol = len(a[0])  # 11 in short data, longer in real file
maxline = maxindex - 1   #10 in short data file, longer in real file

def findtrees(maxcol, maxline, col_inc, line_inc):
    line = 0
    col = 0
    trees = 0
    while True:
        col = col + col_inc
        if col >= maxcol:
            col = col - maxcol
        line = line + line_inc
        if line > maxline:
            #print(f"total trees = {trees}")
            print(f"col_inc = {col_inc}, line_inc = {line_inc}, foundtrees = {trees}")
            return trees
            #break
        current = a[line]
        print (f"col={col}, line={line}, linelen={len(current)}")
        val = current[col]
        if val == "#":
            trees = trees + 1
        print (f"val={val}, trees = {trees}")

mul = 1
#col_inc = 3
#line_inc = 1
foundtrees = findtrees(maxcol, maxline, 1, 1)
mul = mul * foundtrees
foundtrees = findtrees(maxcol, maxline, 3, 1)
mul = mul * foundtrees
foundtrees = findtrees(maxcol, maxline, 5, 1)
mul = mul * foundtrees
foundtrees = findtrees(maxcol, maxline, 7, 1)
mul = mul * foundtrees
foundtrees = findtrees(maxcol, maxline, 1, 2)
mul = mul * foundtrees

print(f"final mul = {mul}")