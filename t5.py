while_list = []
i = 0
j = 0
print("list before loop", while_list)

while i < 10:
    while_list.append(i)
    i = i + 1

print("new_list :", while_list)

while j < i:  # Fix the increment here
    print("remove element is :", while_list.pop())
    print("remaining element ", while_list)
    j += 1  # Fix the increment here
