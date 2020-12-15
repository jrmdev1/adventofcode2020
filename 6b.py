#Advent of code
# 12/13/2020 day6 6b
filename = "data6.txt"
file = open(filename)
filestr = file.read()
a_list = filestr.split("\n\n")
maxindex = len(a_list)
print(a_list)
print(f"maxindex={maxindex}, maxcolumns={len(a_list[0])}")

# ['abc', 'a\nb\nc', 'ab\nac', 'a\na\na\na', 'b']
b_list = []
for b in a_list:
    # combine all members of each group together.
    b_new = b.replace("\n", " ")
    b_list.append(b_new)
# ['abc', 'a b c', 'ab ac', 'a a a a', 'b']

print(b_list)

totalCount = 0
for b in b_list:
    letters = [0]*27
    group_list = b.split(" ")
    print(f"group_list={group_list}")
    count = 0
    for i in range(ord('a'), ord('z')+1):
        saidYes = True
        for personstring in group_list:
            #chr(i)
            if chr(i) not in personstring:
                saidYes = False
                break
        if saidYes:
            count = count + 1
    print(f"b={b}, count={count}")
    totalCount = totalCount + count

print(f"totalCount = {totalCount}")
    