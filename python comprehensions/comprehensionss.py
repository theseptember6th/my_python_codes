#let us suppose i want a list that are multiple of 3 from 0 -99
#1st method normal method but very long

# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# print(ls)

#second method comprehension shortcut method
# ls=[i for i in range(100) if i%3==0] #gets stored in i each time and then the list


#if i want with dictionary such that {0:item0,1:item1,2:item2, and so on}
# dict={i:f"item{i}" for i in range(10)}
# print(dict)

#to reverse the any dictionary by key:value to value:key
# print("reversed dictionary")
# dict_reverse={value:key for key,value in dict.items()}
# print(dict_reverse)


#if i want to perform with set

# dresses={i for i in ["dress1","dress2","dress2","dress2"]}
# print(dresses) #you know how set works so it will take unique dresses only

#for generator

# evens=(i for i in range(11) if i%2==0)
# print(evens.__next__())
# print(evens.__next__())


#simple program taking input from list as user and asking which comprehension he/she wants set comprehension,dictionary,or list

lst=[]
while(1):
    print("1-add item\n 2-exit")
    choice=int(input())
    if choice==1:
        item=input("item: ")
        lst.append(item)
    else:
        break    

print("which comprehension you want to make")
print("1-set comprehension,2-dict comprehension,3-list comprehension")
choice=int(input())
if choice==1:
    set_={i for i in lst}
    print(set_)
elif choice==2:
    dict_={i:f"item{i}" for i in lst}
    print(dict_)
elif choice==3:
    lst1=[i for i in lst]
    print(lst1)
else:
    print("invalid choice")

        
