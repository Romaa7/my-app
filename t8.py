my_list=[6,4,8,2,1,5,7,8]
count=0
for num in my_list:
    if num==5 or num==7:
     continue
    else:
        count=count+num
print(count)
