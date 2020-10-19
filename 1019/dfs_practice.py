'''
스택을 이용한 dfs

정점, 간선수
간선정보
시작점 : 1

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

출력결과

1 3 7 6 5 4 2

'''

def dfs(n, V): #n : 현재 정점
    stack = [0] * (V+1)
    top = 0
    stack[0] = n
    visited[n] = 1

    while top >= 0:
        n = stack[top]
        top -= 1
        print(n, end=" ")
        for i in range(1, V+1):
            if G[n][i] == 1 and visited[i] == 0:
                top += 1
                stack[top] = i
                visited[i] = 1

N, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0] * (N+1) for _ in range(N+1)]
visited =[0] * (N+1)

for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

dfs(1, N)