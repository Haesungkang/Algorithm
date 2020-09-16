import sys
sys.stdin = open('input.txt', "r")

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def dfs(r, c):
    global cnt
    visited[r][c] = 1

    for k in range(4):
        nr = r + dr[k]
        nc = c + dr[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        if blank[nr][nc] == 1: continue
        if visited[nr][nc] == 1: continue
        if blank[nr][nc] == 0:
            dfs(nr, nc)

    #4군데 다 막혔다면 cnt 하나추가하고 빠져나오기
    cnt += 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
maxnumber = []
for row in arr:
    maxnumber.append(max(row))
number = max(maxnumber)
result = []
#print(number)

for water in range(2, number+1):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    blank = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] <= water:
                blank[i][j] = 1
    for row in blank:
        print(row)
    print()

    cnt = 0

    for i in range(N):
        for j in range(N):
            if blank[i][j] == 0:
                dfs(i, j)
                for row in visited:
                    print(row)
                print()

    result.append(cnt)

print(result)
print(max(result))



