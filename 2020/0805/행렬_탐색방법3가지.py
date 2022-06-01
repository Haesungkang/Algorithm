# arr = [[1,2,3,4],[5,6,7,8],[9.10,11,12]]
#
# print(len(arr)) # 행길이
# print(len(arr[0])) # 0번행의 데이터 길이 -> 열길이
# # 행우선순회
#
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         print(arr[i][j], end=' ')
#     print()
#
# #지그재그
# N = len(arr)
# M = len(arr[0])
# for i in range(N):
#     #짝수 행일때
#     if i % 2 == 0:
#         for j in range(M):
#             print(arr[i][j], end=' ')
#     #홀수행일때
#     else:
#         for j in range(M-1,-1,-1):
#             print(arr[i][j], end=' ')
#     print()

#델타 : 변화량 (현재위치기준), 상하좌우 탐색

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12,]]
'''
        -1,0
    0,-1 0,0 0,1
         1,0        
'''
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(4):
    nx = 1 + dx[i] #내 현재 위치 1.1
    ny = 1 + dy[i]
    print(arr[nx][ny])


