


class Node:
    def __init__(self, cargo, leaves=[]):
        self.cargo = cargo
        self.leaves = leaves

    def __str__(self):
        return str(self.cargo)
    
    def add(self, parent, child):
        if self.cargo == parent:
           self.leaves[:]=child
           return(True)
        else:
           for leaf in self.leaves:
              leaf.add(parent,child)

def print_tree(tree):
    if tree == None: return 0
    print("-",tree.cargo)
    for leaf in self.leavese:
       print_tree(leaf)


input_test="COM)B, B)C, C)D, D)E, E)F, B)G, G)H, D)I, E)J, J)K, K)L"

orbits=input_test.split(",")

root_object,o2=orbits[0].split(")")

orbittree=Node(root_object)
for orbit in orbits:
   object1,object2=orbit.split(")")
   orbittree.add(object1,object2)

print_tree(orbittree)


