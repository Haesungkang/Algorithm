#num = [int(n) for n in input()] # '49679' -> 하나를 읽어들인다음에 한숫자씩 n으로 넣고 n을 int형변환후 리스트전환

#버블정렬
def bubblesort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i): # bubble sort의 개념을 다시 생각해보면서 i가 왜들어가는지 생각해보기
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

#카운팅정렬
def Counting_Sort(A, K):
    # 입력배열 A[1...n]
    # 정렬된배열 B[1...n]
    # 카운트배열 C[1....n]
    B = [0] * len(A)
    C = [0] * (K+1)

    for i in range(len(B)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    # for i in range(len(B)-1, -1, -1):
    #     B[C[A[i]] - 1] = A[i]
    #     C[A[i]] -= 1

    for i in reversed(range(len(A))):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

    return B
A=[2,0,2,0,4,1,5,5,2,0,2,4,0,4,0,3]
print(Counting_Sort(A, 5))

#이진탐색
def bin_search(a,key):
    start = 0
    end = len(a)-1
    while start <= end:
        middle = (start + end) // 2
        # ==
        if a[middle] == key:
            return True, middle  # python의 경우 tuple의 값으로 넘길수있다
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
        # <
        # >
    return False, -1

# 2차원 배열 input받는법
#arr = [list(map(int, input().split())) for _ in range(N)] #한줄배열을 잡고 그다음에 range시키는느낌
blank = [[0 for _ in range(10)] for _ in range(10)]
print(blank)

# 비트연산 - 부분집합
arr = [1,2,3]
N = len(arr)
for i in range(1<<N):
    for j in range(N):
        if i & (1 << j):
            print(arr[j], end = " ")

    print()

#선택정렬
def selectionSort(a):
    # i : 0 ~ len(n) -1
    for i in range(len(a)-1):   # 0, 1, 2, 3
        # 최소값 찾기
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]

# arr = [64, 25, 10, 22, 11]
# selectionSort(arr)
# print(arr)


#bruteforce
p = "is"
t = "This is a book!"
M = len(p)
N = len(t)
def bruteForce(p, t):
    i = 0
    j = 0
    while j < M and i < N :
        if t[i] != p[j]: # 매칭에 실패하면
            i = i -j
            j = -1 # 24번행에서 +1하면 0으로 변경되므로 -> 첫번째 패턴문자로 이동
        i += 1
        j += 1
    if j == M : return i - M
    else: return -1

# dfs재귀
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v):
    # 방문 체크
    visited[v] = 1
    print(v, end = " ")
    # v의 인접한 정점중에서 방문안한 정점을 재귀호출
    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

# 정점, 간선
N, E = map(int, input().split())
# 간선들.....
temp = list(map(int, input().split()))
# 인접행렬
G = [[0] * (N+1) for _ in range(N+1)]
# 방문체크
visited = [0] * (N+1)
# 간선들을 인접행렬에 저장
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

dfs(1)


# dfs stack
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

# Stack 괄호검사 예시
for tc in range(1, int(input()) + 1):
    arr = input()
    S = []

    # 한문자씩 읽어서 처리
    ans = 1
    for ch in arr:
        if ch == '(' or ch == '{':
            S.append(ch)
        if ch == ')' or ch == '}':
            # 빈스택일경우
            if len(S) == 0:
                ans = 0;
                break
            t = S.pop()
            if (ch == ')' and t != '(') or (ch == '}' and t != '{'):
                ans = 0;
                break
        # else: #안해도된다
    if len(S) == 0:  # 빈스택인지조사
        ans = 0
    print(ans)
