#Advent of code
# 12/2/2020 Day1b

#a = [ 1721, 979, 366, 299, 675, 1456 ]
filename = "numbersday1.txt"
file = open(filename)
filestr = file.read()
a_str = filestr.split("\n")
print (a_str)
a = [int(i) for i in a_str]
#print(a)
#exit()

maxindex = len(a)
for i in range(maxindex):
    #print(i)
    for i2 in range(i+1, maxindex):
        for i3 in range(i2+1, maxindex):
            print(i, i2, i3)
            sum = a[i] + a[i2] + a[i3]
            print(f"sum = {sum}")
            if sum == 2020:
                print(f"Found answer {a[i]} + {a[i2]} + {a[i3]} = 2020")
                mul = a[i] * a[i2] * a[i3]
                print(f"multiplied out = {mul}")
                exit()
    

