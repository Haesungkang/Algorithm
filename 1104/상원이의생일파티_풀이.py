import sys
sys.stdin = open('sample_input.txt', 'r')

def bfs(v): #v : 시작점
    q = []
    q.append(v) # 시작점 넣기
    visited[v] = 1
    cnt = 0
    level = 0
    while q:
        #레벨은 나누기위한 작업 s=len(q)
        s = len(q) #현재큐의 길이
        # 단순 반복을 위한 작업이므로 _로 대체 가능
        for _ in range(s):
            t = q.pop(0)    #큐에서 하나 가져옴
            #for i in range(N+1): 인접리스트로불렀기때문에 이렇게 for구문 돌릴필요가 없음
            for i in adj[t]:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1
        level += 1
        if level == 2: break
    return cnt

T = int(input())
for tc in range(1, T+1):
    #### 그래프 표현 -> 인접 리스트 ######
    N, M = map(int, input().split())
    adj = {i:[] for i in range(N+1)} # 인접리스트 초기화
    for i in range(M):  #간선의 갯수만큼 반복
        a,b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)    #무방향그래프

    #print(adj)
    visited = [0] * (N+1)
    print("#{} {}".format(tc, bfs(1)))