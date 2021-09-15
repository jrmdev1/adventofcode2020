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
#print(f"maxrows={maxrows}")
guesses = [int(i) for i in a_list[0].split(",")]
print(guesses)
#guesses = dict(guesses)
lastGuess = 0
for i in range(len(guesses), 2019):
    print(f"i={i}")
    lastGuess = guesses[i-1]
    n = guesses.count(lastGuess)
    if n <= 1:
        # first time for previous num
        guesses.append(0)
        print(f"added 0")
    elif n>1:
        # previously spoken
        reverse = guesses[::-1]
        for r, rval in enumerate(reverse):
            # skip first
            print(f"r={r}, rval={rval}")
            if rval == lastGuess:
                pass
    else:
        print(f"ERROR!, n == {n} lastGuess={lastGuess}")
        break


print(f"i={i}, guesses[i]={guesses[i]}")