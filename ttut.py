def int_to_ascii(integer):
    return chr(integer)

try:
    num = int(input("Enter a positive integer: "))
    result = int_to_ascii(num)
    print(f"The ASCII character for {num} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
print("______________________________________________________")
######################################################
num=int(input("Enter posative number"))
def ASCII_value(num):
       return chr(num)
print("ASCII for the num is :",ASCII_value(num))