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
result = []
result.append(a)
def dfs(x):
    visited[x] = 1
    if x == b:
        return 
    else:
        for w in range(n+1):
            if arr[x][w] == 1 and visited[w] == 0:
                result.append(w)
                dfs(w)

dfs(a)
#print(result)
chon1 = 0
chon2 = 0
cnt = 0
for i in range(len(result)):
    if result[i] == a:
        cnt += 1
        chon1 = i

for j in range(len(result)):
    if result[j] == b:
        cnt += 1
        chon2 = j

#print(chon1, chon2)

if abs(chon1-chon2) > 0 and cnt == 2:
    print(abs(chon1-chon2))
else:
    print(-1)



