import sys
sys.stdin = open('input.txt', 'r')

arr = [list(map(int,input().split())) for _ in range(5)]
print(arr)

N = len(arr)
M = len(arr[0])
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for x in range(N):
    list2 = []
    for y in range(M):
        list1 = []
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if testX >= 0 and testX < N and testY >= 0 and testY <M :
                list1.append(arr[testX][testY])

        list2.append(list1)
    print(list2)
    
# for i in range(len(list2)):
#     subtract = 0
#     for j in range(len(list2[i])):
#         print(list2[i][j])
#         if arr[i][j] >= list2[i][j]:
#             subtract += (arr[i][j]-list2[i][j])
#         else:
#             subtract += (list2[i][j] - arr[i][j])
#     print(subtract)

#11 10 8 4 7
#15 11 17 9 12
#9 11 10 10 12
#9 21 11 10 7
#5 10 11 16 8