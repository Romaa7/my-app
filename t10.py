list1=[1,3,5,7,89,10]
list2=[2,59,69,86,19]
list3=[5,90,30,50,20]
max_list=[]
min_list=[]
x=max(list1)
y=max(list2)
z=max(list3)
#by append eaach element alone 
max_list.append(x)
max_list.append(y)
max_list.append(z)
#by extend all element in the list at once time
max_list.extend([x,y,z])
i=min(list1)
j=min(list2)
k=min(list3)

min_list.append(i)
min_list.append(j)
min_list.append(k)
min_list.extend([i,j,k])
print("The max number of lists:",max_list)
print("The min number of lists:",min_list)

