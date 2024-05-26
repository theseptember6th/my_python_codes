rows=int(input("enter no of rows for star pattern"))
print("press 1 - for foward star pattern")
print("press 0 - for backward star pattern")
x=int(input())  #required
decider=bool(x)


def backwardstarpattern(rows):
    for i in range(rows):
        for j in range(rows,i,-1):
            print("*",end="")
        print("")


def forwardstarpattern(rows):
    for i in range(rows):
        for j in range(0,i+1,1):
            print("*",end="")
        print("")    



if decider==True:
    forwardstarpattern(rows)
else:
    backwardstarpattern(rows)   

