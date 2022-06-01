import sys
sys.stdin = open("sample_input_3.txt","r")
'''
V는  숫자
E는 노드개수 
S, G는 출발 끝 지점
'''
def dfs(n, V):
    stack = [0] * V
    visited = [0] * (V+1)
    visit = []
    top = -1

    top += 1
    stack[top] = n
    visited[n] = 1

    while top >= 0:
        n = stack[top]
        top -= 1
        visit.append(n)
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0:
                top += 1
                stack[top] = i
                visited[i] = 1
    return visit
T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
    S, G = map(int, input().split())
    # for row in adj:
    #     print(row)
    result = dfs(S, V)
    truetime = 0
    for i in range(len(result)):
        if result[0] == S and result[i] == G:
            truetime += 1
    if truetime != 0:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))

