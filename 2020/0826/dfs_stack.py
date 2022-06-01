'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(n, V): #n : 현재 정점
    stack = [0] * V # 스택
    visited = [0] * (V+1) # 방문배열
    top = -1

    top += 1
    stack[top] = n #시작정점을 스택에 넣기
    visited[n] = 1 #시작정점을 방문했다고 표시

    while top >= 0:  #스택이 비어있지 않는 동안 반복
        n = stack[top] #스택에서 하나 꺼내오기
        top -= 1
        print(n, end=" ")
        for i in range(1, V+1):
            # n에 인접하고 아직 방문하지 않은 정점 i라면
            if adj[n][i] == 1 and visited[i] == 0:
                top += 1
                stack[top] = i
                visited[i] = 1 #방문여부를 체크, 스택에 이미 한번 방문했으니 바로 적용시켜서 나중에 다시 스택안쌓이게

V, E = map(int, input().split())
# 인접행렬을 생성
adj = [[0] * (V+1) for _ in range(V+1)]
# for row in adj:
#     print(row)
edges = list(map(int, input().split())) # 간선정보가져오기
for i in range(E):
    n1, n2 = edges[i*2],edges[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 이걸하나만 하면 방향그래프

dfs(1,V)