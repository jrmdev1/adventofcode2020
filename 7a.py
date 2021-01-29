#Advent of code
# 01/21/21 (start 12/14/2020) day7 7a
import re
# pip3 install treelib
from treelib import Node, Tree

filename = "data7.txt"
file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
maxindex = len(a_list)
print(a_list)
print(f"maxindex={maxindex}, maxcolumns={len(a_list[0])}")

#muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
#plaid coral bags contain 2 pale green bags, 2 faded tomato bags, 2 dark salmon bags, 1 vibrant magenta bag.
#faded blue bags contain no other bags.

# parse the file (try regex)
# make list of lists, to show connections.
# go backwards from the shiny gold bags.

# can make an initial test case parsing and finding the top level holders of shiny gold.
tree = Tree()
tree.create_node("root", "root")    # create root, (tag, identifier)
tree.create_node("shiny gold", "shiny gold", parent="root")    # create root, (tag, identifier)
tree.show()

for b in a_list:
    # TODO: parse the comma(s) afterwards for other groups!
    m = re.match(r"(\w+ \w+) (?:bags) (?:contain) (\w+) (\w+ \w+) (?:bags*)", b)
    # grpall = m.group(0)
    # print(f"{grpall}")  # string
    print(f"{m.groups()}")    # string in groups, indexed 1 and up.
    #print(f"len={len(grpall)}, span={m.span()}")
    child = m.group(1)  # first entry
    par = m.group(3)
    child_list = []
    child_list.append(child)
    cnt_other = b.count(',')
    print(f"cnt_other={cnt_other}")
    if cnt_other > 0:
        remain_list = b.split(", ")
        remain_list.pop(0)    # drop already processed child and parent string entry
        print(f"remain_list={remain_list}")
        for i in range(0, cnt_other):
            m = re.match(r"(\w+) (\w+ \w+) (?:bags*)", remain_list[i])
            num = m.group(1)
            child = m.group(2)
            print(f"child={child}")
            child_list.append(child)

    for child in child_list:
        if tree.contains(par):
            tree.create_node(child, child, parent=par)
        else:
            # add to root until we can find its true parent (later)
            tree.create_node(child, child, parent="root")
    
    tree.show()

    # count = 0
    # for c in m.groups():
    #     #print(f"{c}")
    #     count = count +1
    # print(f"count = {count}")

tree.show()


# the group is as shown afterwards: (child, count, THEN parent)
# shiny gold is the parent.
# vibrant plum bags contain 5 faded blue bag, 6 dotted black bags.
# ('vibrant plum', '5', 'faded blue')
# >>> import re      # split, search, match
# >>> m = re.search('(?<=abc)def', 'abcdef')
# >>> m.group(0)
#m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")