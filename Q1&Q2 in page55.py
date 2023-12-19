for i in range(102):
    for j in range(102):
      if i % 5==0 and j%5==0:
          sum=j+i
          print(i,"+",j,"=",sum)
print("-----------------------")
n=int(input("enter the value  you want to get the facturail of it:" ))
F=1
for i in range(1,n+1):
     F=F*i
print("fact of n is =",F)



