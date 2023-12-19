
def Summation(num1,num2):
    sum=num1+num2
    return sum
def Subtraction(num1,num2):
    sub=num1-num2
    return sub
def Multiplication(num1,num2):
    mul=num1*num2
    return mul
def Division(num1,num2):
    div=num1/num2
    return div
flag=1
while flag:
    print("\t\tChoose which operation you need to preform :")
    print("\t\tFor Summation :press 1 ")
    print("\t\tFor Subtraction :press 2 ")
    print("\t\tFor Multiplication :press 3 ")
    print("\t\tFor Division :press 4 ")
    print("\t\tpress o to exit")
    user_input=int(input())
    if user_input ==1:
        num1=int(input("Enter the first num"))
        num2= int(input("Enter the second num"))
        res=Summation(num1,num2)
        print("The sum:",res)
    elif user_input ==2:
        num1=int(input("Enter the first num"))
        num2= int(input("Enter the second num"))
        res=Subtraction(num1,num2)
        print("The sub:",res)

    elif user_input ==3:
        num1=int(input("Enter the first num"))
        num2= int(input("Enter the second num"))
        res=Multiplication(num1,num2)
        print("The mul: ",res)
    elif user_input ==4:
        num1=int(input("Enter the first num"))
        num2= int(input("Enter the second num"))
        res=Division(num1,num2)
        print("The div:",res)
    elif user_input==0:
        flag=0
    else:
        print("Please Enter valied chooes")