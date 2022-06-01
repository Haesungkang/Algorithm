import sys
sys.stdin = open('input5.txt', 'r')

def dfs(v):
    global result
    visited[v] = 1

    for w in range(C+1):
        if temp[v][w] == 1 and visited[w] == 0:
            result += 1
            dfs(w)



C = int(input())
N = int(input())
temp = [[0] * (C+1) for _ in range(C+1)]
visited = [0] * (C+1)

for i in range(N):
    s, e = map(int, input().split())
    temp[s][e] = temp[e][s] = 1

result = 0

dfs(1)
print(result)
# for row in temp:
#     print(row)