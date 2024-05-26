# 0 1 1 2 3 5 8
# 1 2 3 4 5 6 7
def fibonacci_recursion(n): #nth term
   if n==1:
        return 0
   elif n==2:
        return 1
   else:
       return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)

print(fibonacci_recursion(7))