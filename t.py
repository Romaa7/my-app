for i in range(5):
   print( i**2)
print("_____________________")

#code retrn  i**2 but i encrease i**2 in each step

i = 1
while i < 100:
 print(i ** 2)
 i += i ** 2
print("_________________________")
#find the prime numbers
max_n =int(input("enter the end of the loop"))
for n in range(2, max_n):
  for x in range(2, n):
     if n % x == 0:  # n divisible by x
        print(n, " equals", x, " * ",int(n / x))
        break
  else: # executed if no break in for loop
#loop fell through without finding a factor

   print(n,"is a prime number")
print("_________________________________")

# Example for explin the local or global
def function1(x):
 def function2(y):
      print (y + 2)
      return y + 2
 return 3 * function2(x)
# call the function
a = function1(2) # what is the output:(y+2)and 3*(y+2)
print( a)
b = function2(2.5) # what is the result of that: error
print("__________________________")
# Example
x = 0
def incr_x():
 x = x + 1 # does not work
 def incr_x2():
   global x
x = x + 1 # does work
print("______________________")
#scope
def f1():
 global x
 x = x + 1
 return x
def f2():
 return x+1
def f3():
 x = 5
 return x+1
x = 0
print( f1())
print (f2())
print( f3())

