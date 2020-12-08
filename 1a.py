#Advent of code
# 12/1/2020 Day1a



#a = [ 1721, 979, 366, 299, 675, 1456 ]
filename = "numbers.txt"
tickerFile = open(filename)
tickerStr = tickerFile.read()
a_str = tickerStr.split("\n")
print (a_str)
a = [int(i) for i in a_str]
#print(a)
#exit()

maxindex = len(a)
done = False
for i in range(len(a)):
    #print(i)
    for i2 in range(i+1, maxindex):
        print(i, i2)
        sum = a[i] + a[i2]
        print(f"sum = {sum}")
        if sum == 2020:
            print(f"Found answer {a[i]} + {a[i2]} = 2020")
            mul = a[i] * a[i2]
            print(f"multiplied out = {mul}")
            done = True
            exit()
    

