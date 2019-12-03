import math

tests1=[[[1,0,0,0,99],[2,0,0,0,99]],[[2,3,0,3,99],[2,3,0,6,99]],[[2,4,4,5,99,0],[2,4,4,5,99,9801]],[[1,1,1,4,99,5,6,0,99],[30,1,1,4,2,5,6,0,99]]]

#tests2=[[14,2],[1969,966],[100756,50346]]


def print_current_state(prog,i):
    print(prog)
    for j in range(0, i-1):
        print("", end=" ")
    print(i)

def run_program(prog):
    i=0
    while (i < len(prog)):
        code=int(prog[i])
        if (code==99):
            break
        input1=prog[i+1]
        input2=prog[i+2]
        output=prog[i+3]
        #print_current_state(prog,i)
        if (code==1):
            prog[output]=prog[input1]+prog[input2]
        elif (code==2):
            prog[output]=prog[input1]*prog[input2]
        elif (code==99):
            break
        i=i+4
    return(prog)

def check_tests1(tests):
    for test in tests:
        if (run_program(test[0])==test[1]):
            print("Yay")
        else:
            print(test[0]," value should be ", test[1], " but is ", calculate_fuel(test[0]))

def part_one():
    with open('input/day2.txt') as fp:
        line=fp.readline()
        line=line.strip()
        program=line.split(",")
        for i in range(0, len(program)):
            program[i]=int(program[i])
        program[1]=12
        program[2]=2
        prog=run_program(program)


def evaluate_program(p,noun,verb):
    
    p[1]=noun
    p[2]=verb
    pnew=run_program(p)

    return(pnew[0])


def part_two():
    with open('input/day2.txt') as fp:
        line=fp.readline()
        line=line.strip()
        program=line.split(",")
        for i in range(0, len(program)):
            program[i]=int(program[i])
    for n in range (0 , 99):
        for v in range (0, 99):
            x=evaluate_program(program[:],n,v)
            if (x==19690720):
                print("noun = ",n," and verb = ",v)
                print(100*n+v)



#check_tests1(tests1)
#check_tests2(tests2)
#part_one()
part_two()


