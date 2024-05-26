#iterative approach

def factorial_iterative(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac


def factorial_recursion(n):
    fac=1
    if(n==1):
        return 1
    elif(n==0):
        return 1
    else:
        return n*factorial_recursion(n-1)

print("factorial using iteration ",factorial_iterative(5))
print("factorial using recursion ",factorial_recursion(5))
