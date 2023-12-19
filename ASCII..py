def int_to_ascii(integer):
    if integer < 0:
        return "Invalid input. Please provide a positive integer."
    elif integer > 127:
        return "ASCII value out of range (0-127)."
    else:
        return chr(integer)

# Example usage:
try:
    num = int(input("Enter a positive integer: "))
    result = int_to_ascii(num)
    print(f"The ASCII character for {num} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
print("___________________________________________________________")
num=int(input("Enter posative number"))
def ASCII_value(num):
       return chr(num)
print("ASCII for the num is :",ASCII_value(num))
print("___________________________________________________________")
str=input("Enter the value that you want to know it is ASCII NUMBER:")
def ASCII_NUM(str):
    return ord(str)
print("The ASCII Numder Is :",ASCII_NUM(str))
