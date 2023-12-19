emp_list=[]
emp_list.insert(10,6)
#print(emp_list)
list1=[x for x in range(10)]
print(list1)
list1.sort(reverse=True)
print(list1)
print("__________________________")


def sum_num(number_list):
    total = 0
    for number in number_list:
     total+=number
    return total
user_input=input("enter list of numbers :")
numbers=[int(x) for x in user_input.split()]
res= sum_num(numbers)
print( "sum of numbers",res)

print("_______________________-")
def sum_of_numbers(number_list):
    total = 0
    for number in number_list:
        total += number
    return total

# Input from the user
user_input = input("Enter a list of numbers separated by spaces: ")
# Convert the input string to a list of integers
numbers = [int(x) for x in user_input.split()]

result = sum_of_numbers(numbers)
print("Sum of numbers:", result)






