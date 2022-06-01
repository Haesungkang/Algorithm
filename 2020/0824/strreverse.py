def str_reve(str):
    arr = list(str)
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
        str = ''.join(arr)
        return str

str = 'algorithm'
str1 = str_rev(str)
print(str1)