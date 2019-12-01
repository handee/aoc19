import math

tests1=[[12,2],[14,2],[1969,654],[100756,33583]]

tests2=[[14,2],[1969,966],[100756,50346]]

def calculate_fuel(mass):
    ret_val=math.floor(mass/3)-2
    if ret_val<0:
        ret_val=0
    return(ret_val)

def calculate_fuelfuel(mass):
    fuelmass=calculate_fuel(mass)
    accmass=fuelmass #accumulated fuel mass
    while (fuelmass>0):
        fuelmass=calculate_fuel(fuelmass)
        accmass=accmass+fuelmass
    return accmass  

def check_tests1(tests):
    for test in tests:
        if (calculate_fuel(test[0])==test[1]):
            print("Yay")
        else:
            print(test[0]," value should be ", test[1], " but is ", calculate_fuel(test[0]))

def check_tests2(tests):
    for test in tests:
        if (calculate_fuelfuel(test[0])==test[1]):
            print("Yay")
        else:
            print(test[0]," value should be ", test[1], " but is ", calculate_fuelfuel(test[0]))




def part_one():
    fuel=0
    with open('input/day1.txt') as fp:
        line=fp.readline()
        while line:
            m=int(line.strip())
            fuel=fuel+calculate_fuel(m)
            line=fp.readline()

    print("The space ship requires", fuel, "fuel.")

def part_two():
    fuel=0
    with open('input/day1.txt') as fp:
        line=fp.readline()
        while line:
            m=int(line.strip())
            fuel=fuel+calculate_fuelfuel(m)
            line=fp.readline()

    print("The space ship requires", fuel, "fuel.")



#check_tests1(tests1)
#check_tests2(tests2)
#part_one()
part_two()


