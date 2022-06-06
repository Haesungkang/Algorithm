import sys
sys.stdin = open("2022/0601/inputfolder/bfsinput.txt", "r")
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(v):
    # 큐, 방문
    Q = []
    visit = [0] * (V+1)
    # enQ(v), visit(v)
    Q.append(v)
    visit[v] = 1
    #하단부분에 원하는 부분을 실행
    print(v, end = " ")
    # 큐가 비어있지 않은 동안
    while Q:
        # v = deQ()
        v = Q.pop(0)
        # v의 인접한 정점(w), 방문안한 정점이면
        for w in range(1, V+1):
            if G[v][w] == 1 and visit[w] == 0:
            # enQ(w), 방문처리(w)
                Q.append(w)
                visit[w] = 1
                print(w, end=" ")

# 입력 -> 인접행렬
V, E = map(int, input().split())
temp = list(map(int, input().split()))
# 인접행렬 초기화
G = [[0] * (V+1) for _ in range(V+1)]
# 인접행렬 저장
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e] = G[e][s] = 1

for i in range(1, V+1):
    print("{} {}".format(i, G[i]))


## BFS 두번째

# import sys
# sys.stdin = open("input.txt", "r")
# '''
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# '''
# def (v):
#     Q = []
#     visit = [0] * (V+1)

#     #endQ
#     Q.append(v)
#     visit[v] = 1
#     print(v, end = " ")
#     while Q:
#         v = Q.pop(0)
#         for w in G[v]:
#             if not visit[w]:
#                 Q.append(w)
#                 visit[w] = 1
#                 print(w, end=" ")

# # 입력 -> 인접리스트
# V, E = map(int, input().split())
# temp = list(map(int, input().split()))
# # 인접 리스트
# G = [[] for _ in range(V+1)]
# visit = [0] * (V+1)

# for i in range(E):
#     s, e = temp[2*i], temp[2*i+1]
#     G[s].append(e)
#     G[e].append(s)

# print(G)
# (1)
# print()
# # 1에서 가장 멀리 있는 정점의 번호는 얼마이고 몇칸 떨어져 있을까요?

# def 2(v):
#     Q = []
#     visit = [0] * (V+1)

#     #endQ
#     Q.append(v)
#     visit[v] = 1
#     print(v, end = " ")
#     while Q:
#         v = Q.pop(0)
#         for w in G[v]:
#             if not visit[w]:
#                 Q.append(w)
#                 visit[w] = visit[v] + 1
#                 print(w, end=" ")

# visit = [0] * (V+1)
# maxI = 0

# for i in range(1, V+1):
#     if visit[maxI] < visit[i]:
#         maxI = i
# print(maxI, visit[maxI]-1)

# print(G)
# 2(1)
# print()

### BFS Third 메모 

# import sys
# sys.stdin = open("bfsinput.txt", "r")
# '''
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# '''
# def bfs(v):
#     Q = []
#     visit = [0] * (V+1)

#     #endQ
#     Q.append(v)
#     visit[v] = 1
#     print(v, end = " ")
#     while Q:
#         v = Q.pop(0)
#         for w in G[v]:
#             if not visit[w]:
#                 Q.append(w)
#                 visit[w] = visit[v] + 1
#                 print(w, end=" ")

# # 입력 -> 인접리스트
# V, E = map(int, input().split())
# temp = list(map(int, input().split()))
# # 인접 리스트
# # G = [[] for _ in range(V+1)]
# G = {i:[] for i in range(1, V+1)}
# #print(G)
# visit = [0] * (V+1)

# for i in range(E):
#     s, e = temp[2*i], temp[2*i+1]
#     G[s].append(e)
#     G[e].append(s)

# print(G)
# bfs(1)


# def dfs(v):

#     visited[v] = 1
#     print(v, end= " ")
#     for w in range(1, N+1):
#         if G[v][w] == 1 and visited[w] == 0:
#             dfs(w)

# N, E = map(int, input().split())
# temp = list(map(int, input().split()))

# G = [[0 for _ in range(N+1)] for _ in range(N+1)]
# print(G)

# visited = [0] * (N+1)

# for i in range(E):
#     s, e = temp[2*i], temp[2*i+1]
#     G[s][e] = 1
#     G[e][s] = 1

# print(dfs(1))

# def dfs(v):

#     visited[v] = 1
#     print(v, end=" ")
#     for w in range(N+1):
#         if G[v][w] == 1 and visited[w] == 0:
#             dfs(w)

# def bfs(v):
#     visited[v] = 1
#     Q = []
#     Q.append(v)
#     while Q:

#         v = Q.pop(0)
#         for w in range(N + 1):
#             if G[v][w] == 1 and visited[w] == 0:
#                 Q.append(w)
#                 visited[w] = 1
#                 # bfs(w)

# N, E = map(int, input().split())
# temp = list(map(int, input().split()))
# # print(N, E)
# # print(temp)
# G = [[0] * (N+1) for _ in range(N+1)]
# visited = [0] * (N+1)

# for i in range(E):
#     s, e = temp[2*i], temp[2*i+1]
#     G[s][e] = 1
#     G[e][s] = 1

# # for i in G:
# #     print(i)
# dfs(1)