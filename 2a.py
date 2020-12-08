#Advent of code
# 12/6/2020 day2 2a

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
    password = b[1]
    #print(f"{min}, {max}, {letter}, {password}")
    cnt = password.count(letter)
    #print(cnt)
    if cnt >= min and cnt <= max:
        numvalid = numvalid + 1

print(f"numvalid = {numvalid}")

exit()