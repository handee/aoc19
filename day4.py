def is_legal(pw):
    digits=list(pw)
    contains_double=False
    monotonic_increase=True
    for n in range(0, len(digits)-1):
        if (digits[n]==digits[n+1]):
            contains_double=True
        if (int(digits[n])>int(digits[n+1])):
            monotonic_increase=False
    print (digits, monotonic_increase, contains_double)
    if monotonic_increase and contains_double:
        return(True)
    else:
        return(False)

start=124075
end=580769
#start=111111
#end=123456
counter=0

for p in range(start,end):
    if (is_legal(str(p))):
       print("legal")
       counter+=1

print(counter)
