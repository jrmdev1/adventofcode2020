#Advent of code
# 12/9/2020 day4 4b

def isHexLower( char ):
    valid = False
    if (char >= "0" and char <= "9") or (char >= "a" and char <= "f"):
        valid = True
    return valid

def validate( b ):
    # "byr:" in b 
    # "iyr:" in b 
    # "eyr:" in b 
    # "hgt:" in b
    # "hcl:" in b 
    # "ecl:" in b 
    # "pid:" in b 
    # ecl:lzr cid:279 pid:192cm hcl:1f7352 iyr:2014 hgt:70cm eyr:1983 byr:2004
    b_split = b.split()
    #print(b_split)
    #['ecl:lzr', 'cid:279', 'pid:192cm', 'hcl:1f7352', 'iyr:2014', 'hgt:70cm', 'eyr:1983', 'byr:2004']
    #['byr:1937', 'eyr:2021', 'iyr:2017', 'cid:91', 'hgt:183cm', 'hcl:#a97842', 'ecl:blu', 'pid:149192621']
    valid = True
    for field in b_split:
        val = field.split(":")
        field_type = val[0]
        field_val = val[1]
        if field_type == "byr":
            year = int(field_val)
            if year < 1920 or year > 2002:
                valid = False
                break
        elif field_type == "iyr":
            year = int(field_val)
            if year < 2010 or year > 2020:
                valid = False
                break
        elif field_type == "eyr":
            year = int(field_val)
            if year < 2020 or year > 2030:
                valid = False
                break
        elif field_type == "hgt":
            #print(f"len units = {field_val[-2:]}")
            if field_val[-2:] == "cm":
                height = int(field_val[:-2])
                #print(f"val string = {field_val[:-2]}, height = {height}")
                if height < 150 or height > 193:
                    valid = False
                    break
            elif field_val[-2:] == "in":
                height = int(field_val[:-2])
                #print(f"val string = {field_val[:-2]}, height = {height}")
                if height < 59 or height > 76:
                    valid = False
                    break
            else:
                valid = False
                break
        elif field_type == "hcl":
            if field_val[0] != "#":
                valid = False
                break
            color = field_val[1:]
            if len(color) != 6:
                valid = False
                break
            for char in color:
                if not isHexLower(char):
                    valid = False
                    break
        elif field_type == "ecl":
            if field_val != "amb" and field_val != "blu" and field_val != "brn" and field_val != "gry" and field_val != "grn" and field_val != "hzl" and field_val != "oth":
                valid = False
                break
        elif field_type == "pid":
            if len(field_val) != 9:
                valid = False
                break
            if not field_val.isdigit():
                valid = False
                break
        elif field_type == "cid":
            # skip
            pass
        else:
            valid = False
            break

    # temp debug
    if not valid:
        print(f"not valid field_type = {field_type} field_val = {field_val}")

    return valid

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