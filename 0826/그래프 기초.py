'''
그래프
그래프 G는 (V,E)의 집합이다.
    V : 정점의 집합
    E : 간선들의 집합

인접
    (u,v)라는 간선이 있다면
    정점u와 정점v는 "인접하다"라고 함

그래프의 표현
    - 인접행렬
        V*V 크기의 행렬
        두 정점 i,j 잇는 간선이 있다면(인접하면) 행렬의 (i,j)를 1로 하고 아니면 0
    - 인접리스트
        추후설명

- 무방향 그래프
    양방향으로 간선이 있다고 생각해서 인접행렬을 만듬 -> 대칭행렬
- 뱡향 그래프
    대칭이 아님
'''

'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
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
# for row in adj:
#      print(row)