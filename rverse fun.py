

def reverse_fun(str):
    print("The str is :",str)
    reverse_str=""
    index=len(str)

    while index > 0:
      reverse_str=reverse_str+str[index-1]
      index=index-1
    return reverse_str

print("revered str is:",reverse_fun("python"))



