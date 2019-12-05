import math

tests1=[[[1,0,0,0,99],[2,0,0,0,99]],[[2,3,0,3,99],[2,3,0,6,99]],[[2,4,4,5,99,0],[2,4,4,5,99,9801]],[[1,1,1,4,99,5,6,0,99],[30,1,1,4,2,5,6,0,99]]]

#tests2=[[14,2],[1969,966],[100756,50346]]


def print_current_state(prog,i):
    print (i, "= i")
    for j in range(0,len(prog)):
        print("[",j,"] ", end=" ")
        print(prog[j], end=", ")
        if (i==j):
            print("***",end=" ")
        if (j%10==0):
            print(" ")

def parse_opcode(string_version):
    output=[]
    string_version=string_version[::-1] # reverse string
    while (len(string_version) < 5): # padd with zeros
        string_version+='0'
    output.append(int(string_version[0]))
    if (output[0]==9):
        output[0]=99
        cl=1
    if (output[0]<3): #it's 1 or 2 and so has three parameters 
        cl=4 # code length
        for i in range(2,5):
            output.append(int(string_version[i]))
    elif (output[0]<5): #it's 3, 4 so has one parameter
        cl=2 # code length
        output.append(int(string_version[2]))
    elif (output[0]<7): #it's 5 or 6 so has two parameter
        cl=3 # code length
        output.append(int(string_version[2]))
        output.append(int(string_version[3]))
    elif (output[0]<9): #it's 7 or 8 so has three parameter
        cl=4 # code length
        for i in range(2,5):
            output.append(int(string_version[i]))
    return(output,cl)



def run_program(prog,input_param):
    i=0
    while (i < len(prog)):
        opcode,codelength=parse_opcode(str(prog[i]))
        if (opcode[0]==99):
            break
        if (opcode[0]==1): # add
            op1=prog[i+1]
            if (opcode[1]==0):
                op1=prog[op1]
            op2=prog[i+2]
            if (opcode[2]==0):
                op2=prog[op2]
            prog[prog[i+3]]=op1+op2
        elif (opcode[0]==2): # multiply
            op1=prog[i+1]
            if (opcode[1]==0):
                op1=prog[op1]
            op2=prog[i+2]
            if (opcode[2]==0):
                op2=prog[op2]
            prog[prog[i+3]]=op1*op2
        elif (opcode[0]==3): #input
            prog[prog[i+1]]=input_param

        elif (opcode[0]==4): #output
            output=prog[i+1]
            if (opcode[1]==1):
                print("output!!!!!!!!!!!!!!!!",output)
            else:
                print("output!!!!!!!!!!!!!!!!",prog[output])
        elif (opcode[0]==5): # jit 
            op1=prog[i+1]
            if (opcode[1]==0):
                op1=prog[op1]
            if (op1!=0) :
                jump=prog[i+2]
                if (opcode[2]==0):
                    jump=prog[prog[i+2]]
                i=jump
                continue    
        elif (opcode[0]==6): # jif 
            op1=prog[i+1]
            if (opcode[1]==0):
                op1=prog[op1]
            if (op1==0) :
                jump=prog[i+2]
                if (opcode[2]==0):
                    jump=prog[prog[i+2]]
                i=jump
                continue    
        elif (opcode[0]==7): # lessthan 
            op1=prog[i+1]
            if (opcode[1]==0):
                op1=prog[op1]
            op2=prog[i+2]
            if (opcode[2]==0):
                op2=prog[op2]
            if (op1<op2):
                prog[prog[i+3]]=1
            else:
                prog[prog[i+3]]=0
        elif (opcode[0]==8): # equals 
            op1=prog[i+1]
            if (opcode[1]==0):
                op1=prog[op1]
            op2=prog[i+2]
            if (opcode[2]==0):
                op2=prog[op2]
            if (op1==op2):
                prog[prog[i+3]]=1
            else:
                prog[prog[i+3]]=0
       

        i=i+codelength
    return(prog)


def part_two():
    with open('input/day5.txt') as fp:
        line=fp.readline()
        line=line.strip()
        program=line.split(",")
        for i in range(0, len(program)):
            program[i]=int(program[i])
        run_program(program,5)

def check_tests():
    inputdata="3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
  #  inputdata="3,9,7,9,10,9,4,9,99,-1,8"
    program=inputdata.split(",")
    for i in range(0, len(program)):
        program[i]=int(program[i])
    run_program(program,9)



#check_tests()
#check_tests2(tests2)
#part_one()
part_two()
