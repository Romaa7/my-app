def Args(*args):
    sum=0
    for x in args:
        sum=sum+x

    return sum
print("for 1argument the sum is:",Args(3))
print("for 2 argument the sum is:",Args(3,5))
print("for 3 argument the sum is:",Args(3,10,70))
print("for 4 argument the sum is:",Args(3,5,12,-50))
print("for 5 argument the sum is:",Args(3,6,9,50,-60))
print("for 6 argument the sum is:",Args(3,-40,70,-18,-20,8))
print("for 7 argument the sum is:",Args(8,9,53,16,-40,-50,80))

