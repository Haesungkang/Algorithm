'''
0000000111100000011000000111100110000110000111100111100111111001100111
'''

b = list(map(int,input()))
# print(b)
bit = []
#7bit씩 나눠서 배열에 담기
for i in range(len(b)//7):
    bit.append(b[7*i:7*i+7])
for row in bit:
    print(row)
# print(bit)

#2진수 -> 10진수
for i in range(len(bit)):
    sum = 0
    for j in range(7):
        if bit[i][j] == 1:
            sum += 2**j
    print(sum)
