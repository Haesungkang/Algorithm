# arr = [1,2,3]
# n = 3
# for i in range(1<<n):   #1<<3 -> 2^3 -> 8 : 부분집합 경우의수
#     # print(i)
#     for j in range(n):  #원소 비트수 만큼 비트비교
#         if i & (1<<j):
#             # i => 0일때
#             # 0 & 0 -> 0000 & 0001 -> 0
#             # 0 & (1<<1: 0010): 2 -> 0000 & 0010 ->
#             # 하나도 선택안됨
#             # i => 1일때
#             # i
#             print(arr[j], end=' ')
#     print()

data = [-7, -3, -2, 5, 8]
n = len(data)
ans = False
for i in range(1<<n): # 모든경우
    sum = 0
    for j in range(n):
        if i &(1<<j):
            sum += data[j]
    if sum == 0:
        ans = True

print(ans)

