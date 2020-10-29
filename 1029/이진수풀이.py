text = list(input())
N = len(text)
binary = ''
for i in range(int(N)):
    if ord(text[i]) >= 65:
        num = ord(text[i]) - 55
    else:
        num = int(text[i])
    a = 3
    while a >= 0:
        if num >= 2 ** a:
            binary += '1'
            num -= 2 **a
        else:
            binary += '0'
        a -= 1
