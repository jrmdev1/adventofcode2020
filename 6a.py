#Advent of code
# 12/13/2020 day6 6a
filename = "data6.txt"
file = open(filename)
filestr = file.read()
a_list = filestr.split("\n\n")
maxindex = len(a_list)
#print(a_list)
print(f"maxindex={maxindex}, maxcolumns={len(a_list[0])}")

# ['abc', 'a\nb\nc', 'ab\nac', 'a\na\na\na', 'b']
b_list = []
for b in a_list:
    # combine all members of each group together.
    b_new = b.replace("\n", "")
    b_list.append(b_new)

print(b_list)

totalCount = 0
for b in b_list:
    letters = [0]*27
    count = 0
    x = 0
    for i in range(ord('a'), ord('z')+1):
        #chr(i)
        x = x+1
        if chr(i) in b:
            print(f"x={x}")
            letters[x] = 1
    for x in range(0, 27):
        #print(f"x={x}")
        if letters[x] != 0:
            count = count + 1
    totalCount = totalCount + count
    print(f"count = {count}")

print(f"totalCount = {totalCount}")
    