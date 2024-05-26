#l1=["momo","choewmein","pizza","noddles"]
# i=1
# for item in l1:
#     if i%2==0:
#         print(f"this is your food {item}")
#     i+=1    


#but the best way to do is using enumerate..it gives both index and item value
#so i dont have to rely on external variable..also
#code readability increases

l1=["momo","choewmein","pizza","noddles"]
for index,item in enumerate(l1):
    if index%2==0:
        print(f"this is your food {item}")