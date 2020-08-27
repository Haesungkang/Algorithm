import sys
sys.stdin = open("sample_input_3.txt","r")

def DFS(v):
    visit[v] = 1
    if v == e:
        return 1
    for w in range(1, V+1):
        if G[v][w] == 1 and visit[w] == 0:
            #여기서 바로 찾아냈으면 뽑아내기
            if DFS(w) == 1:
                return 1
    # return value를 설정할때 함수가 호출되는 모든 지점에 return을 설정해준다
    return 0


for tc in range(1, int(input()) +1):
    V, E = map(int, input().split())
    # 인접행렬, 정점 번호 1 ~ V
    G = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E): # 간선정보 읽기
        u, v = map(int, input().split())
        G[u][v] = 1

    s, e = map(int, input().split())
    visit = [0] * (V+1)


    print(DFS(s))
