#Advent of code
# 12/9/2020 day4 4b

def validate( b ):
    rtnval = False
    # "byr:" in b 
    # "iyr:" in b 
    # "eyr:" in b 
    # "hgt:" in b
    # "hcl:" in b 
    # "ecl:" in b 
    # "pid:" in b 
    # hcl:#341e13 ecl:brn iyr:2019 pid:589837530 cid:157 byr:1925 hgt:183cm eyr:2020
    b_split = b.split()
    print(b_split)

    rtnval = True
   
    return rtnval

filename = "data4.txt"
file = open(filename)
filestr = file.read()
a_list = filestr.split("\n\n")
maxindex = len(a_list)
#print(a_list)
print(f"maxindex={maxindex}, maxcolumns={len(a_list[0])}")
b_list = []
for b in a_list:
    b_new = b.replace("\n", " ")
    b_list.append(b_new)
#print(b_list)

num_valid = 0
for b in b_list:
    if "ecl:" in b and "pid:" in b and "eyr:" in b and "hcl:" in b and "byr:" in b and "iyr:" in b and "hgt:" in b:
        if validate( b ):
            num_valid = num_valid + 1
            #print(f"{b}\n")
print(f"Number of valid passports = {num_valid}")

#ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
#byr:1937 iyr:2017 cid:147 hgt:183cm

#hcl:#341e13 ecl:brn iyr:2019 pid:589837530 cid:157 byr:1925 hgt:183cm eyr:2020