#Advent of code
# 12/6/2020 day2 2b

filename = "numbersday2.txt"
file = open(filename)
filestr = file.read()
a_str = filestr.split("\n")
#print (a_str)
a = a_str

maxindex = len(a)
numvalid = 0
for i in range(maxindex):
    #print(f"{i}, {a[i]} ")
    b = a[i].split(":")
    #print(b)
    c = b[0].split(" ")
    temp = c[0].split("-")
    min = int(temp[0])
    max = int(temp[1])
    letter = c[1]
    password = b[1].strip()
    #print(f"{min}, {max}, {letter}, {password}")
    cnt = password.count(letter)
    nummatch = 0
    if password[min-1] == letter:
        nummatch = nummatch + 1
    if password[max-1] == letter:
        nummatch = nummatch + 1
    if nummatch == 1:
        numvalid = numvalid + 1

print(f"numvalid = {numvalid}")

exit()