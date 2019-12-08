
from collections import defaultdict


#with open('input/day6.txt') as f:
 # orbits = f.read().splitlines()

    
input_test="COM)B, B)C, C)D, D)E, E)F, B)G, G)H, D)I, E)J, J)K, K)L"

orbits=input_test.split(", ")

d= defaultdict(list) # a dictionary/hash table with keys being objects and values being lists of objects
for orbit in orbits:
   object1,object2=orbit.split(")")
   d[object1].append(object2)

o= {} # another dictionary but not a dictionary of lists this time
def count_orbits(sattelite, counter):
  o[sattelite] = counter
  print("Sattelite = ",sattelite," d[sattelite] = ",d[sattelite])
  for orbiter in d[sattelite]:
    count_orbits(orbiter,counter+1)


count_orbits("COM",0)
print d
print o
total=sum(o.values())
print ("Total orbits  = ",total)


