#Advent of code
# 01/21/21 (start 12/14/2020) day7 7a
import re

filename = "data7.txt"
file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxindex = len(a_list)
print(a_list)
print(f"maxindex={maxindex}, maxcolumns={len(a_list[0])}")

# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
#faded blue bags contain no other bags.

# parse the file (try regex)
# make list of lists, to show connections.
# go backwards from the shiny gold bags.

# can make an initial test case parsing and finding the top level holders of shiny gold.

for b in a_list:
    #m = re.match(r"(\w+) (\w+) (?:bags) (?:contain) (\w+) (\w+) (\w+) (?:bag)", b)
    m = re.match(r"(\w+ \w+) (?:bags) (?:contain) (\w+) (\w+ \w+) (?:bags*)", b)
    grpall = m.group(0)
    print(f"{grpall}")
    print(f"{m.groups()}")
    print(f"len={len(grpall)}, span={m.span()}")
    count = 0
    for c in m.groups():
        print(f"{c}")
        count = count +1
    print(f"count = {count}")

# the group is as shown afterwards:
# vibrant plum bags contain 5 faded blue bag, 6 dotted black bags.
# ('vibrant plum', '5', 'faded blue')
# >>> import re      # split, search, match
# >>> m = re.search('(?<=abc)def', 'abcdef')
# >>> m.group(0)
#m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")