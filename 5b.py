#Advent of code
# 12/11/2020 day5 5b
filename = "data5.txt"
file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxindex = len(a_list)
#print(a_list)
print(f"maxindex={maxindex}, maxcolumns={len(a_list[0])}")

row_offset = [ 64, 32, 16, 8, 4, 2, 1 ]
col_offset = [ 4, 2, 1 ]
saved_seats = [0] * 988

highest_sid = 0
for seat in a_list:
    row_str = seat[0:7]
    col_str = seat[7:10]
    #print(f"{row_str}, {col_str}")
    row_id = 0
    for i, char in enumerate(row_str):
        if char == "B":
            row_id = row_id + row_offset[i]
    col_id = 0
    for i, char in enumerate(col_str):
        if char == "R":
            col_id = col_id + col_offset[i]
    sid = row_id * 8 + col_id
    saved_seats[sid] = 1
    #print(f"row_id = {row_id}, col_id = {col_id}, sid = {sid}")
    if sid > highest_sid:
        highest_sid = sid

print (f"highest_sid = {highest_sid}")

for i in range(0, 987):
    if saved_seats[i] == 0:
        #print(f"seat {i} is open")
        if saved_seats[i-1] != 0 and saved_seats[i+1] != 0:
            print(f"my open seat is {i}")


       



# now find the missing seat(s)
