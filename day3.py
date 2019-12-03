
#w1="R8,U5,L5,D3"
#w2="U7,R6,D4,L4"

#w1="R75,D30,R83,U83,L12,D49,R71,U7,L72"
#w2="U62,R66,U55,R34,D71,R55,D58,R83"

#w1="R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
#w2="U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

dirs= { "U": [0,1],
        "D": [0,-1],
        "L": [-1,0],
        "R": [1,0]
        }


with open('input/day3.txt') as fp:
    w1=fp.readline()
    w2=fp.readline()

print(w1)
print(w2)

def follow_wire(wire):
    xs=[0]
    ys=[0]
    x=0
    y=0
    instructions=wire.split(",")
    for ins in instructions:
        l=int(ins[1:])
        for i in range(0,l):
            x+=dirs[ins[0]][0]
            y+=dirs[ins[0]][1]
            xs.append(x)
            ys.append(y)
    return(xs,ys) 

w1x,w1y=follow_wire(w1)
print("followed wire one")
w2x,w2y=follow_wire(w2)
print("followed wire two")

intersections=[]
distances=[]
lengths=[]
for i in range(0,len(w1x)):
    for j in range(0,len(w2x)):
        if w1x[i]==w2x[j] and w1y[i]==w2y[j]:
            intersections.append([w1x[i],w1y[i]])
            distances.append(abs(w1x[i])+abs(w1y[i]))
            lengths.append(i+j)

print(intersections)
print(distances)
print(lengths)
distances.sort()
print(distances[1])
lengths.sort()
print(lengths[1])
