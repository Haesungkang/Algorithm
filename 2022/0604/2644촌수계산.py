import sys
sys.stdin = open('./2022/inputfolder/2644.txt', 'r')

n = int(input())
a, b = map(int,input().split())
node = int(input())
arr = [[0] * (n+1) for _ in range(n+1)]
for i in range(node):
    i , j = map(int, input().split())
    arr[i][j] = arr[j][i] = 1

visited = [0] * (n+1)
cnt = 0
def dfs(x):
    global cnt
    visited[x] = 1
    if x == b:
        return 
    for w in range(n+1):
        if arr[x][w] == 1 and visited[w] == 0:
            cnt += 1
            dfs(w)
    cnt = 0 

dfs(a)
print(cnt)


