my_list=[11,3,5,6,8,9,10,200,100,6,8,100,11,3]
def Uniqe_list(my_list):
    uniqe_list=[]
    for  num in my_list:
        if num not in uniqe_list:
            uniqe_list.append(num)
            
    return uniqe_list
print("Uniqe list :",Uniqe_list(my_list))