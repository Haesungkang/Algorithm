import sys
sys.stdin = open('sample_input_2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = {i:[] for i in range(V+1)}
    for i in range(E):
        n1, n2, c = map(int, input().split()) # 시작정점, 끝정점, 가중치
        adj[n1].append([n2,c]) # 도착정점, 가중치
    #print(adj)

    INF = 999999 # 큰값
    dist = [INF] * (V+1)  # 각 정점의 최단거리(현재까지의)
    selected = [False] * (V+1)
    # 시작점 : 0번에서 시작
    dist[0] = 0
    cnt = 0
    result = []
    while cnt <= V:
        # 최소값 찾기
        minV = INF
        u = -1
        for i in range(V+1):
            # 아직 최단거리가 결정안되고, 최소의 정점을 선택
            if not selected[i] and minV > dist[i]:
                minV = dist[i]
                u = i
        selected[u] = True
        cnt += 1

        print(adj)
        print(u)
        # 간선완화
        for w, cost in adj[u]:
            #print(w, cost)# 도착정점, 가중치
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost
                result.append(cost)
        #print(1)
    print(dist)
    print(result)
