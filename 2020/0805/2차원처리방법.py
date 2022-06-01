
#1
# N, M = map(int,input(.split()))
# mylist = [0 for _ in range(N)]
# mylist = [0] * N
# for i in range(N):
#     mylist[i] = list(map(int,input().split()))
# print(mylist)
#
# #2
# N, M = map(int,input(.split()))
# mylist = []
# for i in range(N):
#     mylist.append(list(map(int,input().split())))
# print(mylist)

#3
N, M = map(int,input(.split()))
mylist = [list(map(int,input().split())) for _ in range(N)]
print(mylist)

# 0 으로 초기화
# v = [[0] * 3] * 3 -> 이렇게 하면안된다
# print(v)

# N = 3 #행
# M = 4 #열
# v = [[0 for _ in range(M)] for _ in range(N)] # -> 열을 만들고 행을 만들어야 한다 3*4가만들어진다
# print(v)
#
# v = [[0] * M for _ in range(N)]
# print(v)

# for i in range(N):
#     for j in range(i+1, M):
#         # if i < j:
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
# print(arr)

# 조합구하는 방법
arr = [1, 2, 3, 4]
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        # # if i < j:
        #     arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        print((arr[i], arr[j], end=" "))





