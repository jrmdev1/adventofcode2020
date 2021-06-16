#Advent of code
# 06/15/21 day8 8a
#import re

filename = "data8.txt"
file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxindex = len(a_list)
print(a_list)
print(f"maxindex={maxindex}, maxcolumns={len(a_list[0])}")

acc = 0
pc = 0
hasrun_list = [0] * maxindex

while pc >= 0:
    if hasrun_list[pc] != 0:
        print(f"line already run, exiting pc = {pc}, acc = {acc}")
        break
    hasrun_list[pc] = 1
    line = a_list[pc]
    oper, arg = line.split(" ")
    print(f"pc = {pc}, oper = {oper}, arg = {arg}")
    arg_int = int(arg)
    if oper == "nop":
        print(f"nop exec")
    elif oper == "acc":
        acc = acc + arg_int
        print(f"acc new = {acc}")
    elif oper == "jmp":
        pc = pc + arg_int
        print(f"jmp {arg_int}, new pc = {pc}")
        continue        # start processing at new pc, dont increment
    else:
        print(f"ERROR: syntax {line}")
        break
    pc = pc + 1
        
print(f"final pc = {pc}, acc = {acc}")

