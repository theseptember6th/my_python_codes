# It does what it is named, it filters. It filters a list for you according to the function you gave it. It takes two arguments, function name and list name. Function should return true or false. It takes the list and for whatever list item the function returns true, it filters all those items and shows you. Here is an example:

def greater_than_2(n):
    if n>2:
        return True
    else:
        return False

h1 = [1,2,3,4,5,6,7,-2,-5]
greater_th_2 = list(filter(greater_than_2, h1))
print(greater_th_2)