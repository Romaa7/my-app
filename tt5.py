list1=[1,3,5,7,10,15]
list2=[3,19,40,2]
list3=[]
for i in list1:
    for j in list2:
        res=i*j
        print("the value of i:",i)
        print("the value of j:",j)
        print("Append values in :",res)
        list3.append(res)
print("the multuplaction list :",list3)
