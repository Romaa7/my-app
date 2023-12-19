N = int(input("Enter a number:"))
sum = 0
for i in range(1, N+1):
	x = int(input("Enter a value"))
	sum = sum + x
print(sum)
print('----------------------------')
N = int(input("Enter a number: "))
sum = 0
c = 0
for i in range(0, N):
	x = int(input("Enter a value: "))
	if x > 0:
		sum = sum + x
		c = c + 1
avg = sum / c
print(sum)
print(avg)
