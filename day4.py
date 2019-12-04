def is_legalpart1(pw):
    digits=list(pw)
    contains_double=False
    monotonic_increase=True
    for n in range(0, len(digits)-1):
        if (digits[n]==digits[n+1]):
            contains_double=True
        if (int(digits[n])>int(digits[n+1])):
            monotonic_increase=False
    if monotonic_increase and contains_double:
        return(True)
    else:
        return(False)



def is_legalpart2(pw):
    digits=list(pw)
    contains_double=False
    monotonic_increase=True
    for n in range(0, len(digits)-1):
        if (digits[n]==digits[n+1]):
            # there are two in a row. 
            # if there's a digit before, is it different?
            dbf=False #different number before
            dba=False #different number after 
            if n==0: # it's the start of the code
                dbf=True
            elif n > 0 and digits[n-1]!=digits[n]:
                dbf=True
            if n+2>=len(digits):
                dba=True # it's the end of the code
            elif n<len(digits)-2 and digits[n+2]!=digits[n]:
                dba=True 
            if dba and dbf:
                contains_double=True

        if (int(digits[n])>int(digits[n+1])):
            monotonic_increase=False
    if monotonic_increase and contains_double:
        return(True)
    else:
        return(False)



start=124075
end=580769
#start=111111
#end=123456
counter=0
counter2=0

for p in range(start,end):
    if (is_legalpart1(str(p))):
       counter+=1
    if (is_legalpart2(str(p))):
       counter2+=1

print("part 1 ", counter)
print("part 2 ",counter2)


