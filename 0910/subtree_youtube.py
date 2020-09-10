import sys
sys.stdin = open("sample_input.txt", "r")

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())    # E간선수, 정점수 = E+1
    # 정점 번호 1 ~ E+1
    L = [0] * (E+2)
    R = [0] * (E+2)
    P = [0] * (E+2)

    arr = list(map(int, input().split()))
    for i in range(0, E*2, 2): #arr[i] --> arr[i+1]
        p, c = arr[i], arr[i+1]

        if L[p]: R[p] = c
        else: L[p] = c
        P[c] = p
    # global ans이용
    # ans = 0
    # def traverse(v):
    #     global ans
    #     if v == 0: return
    #     ans += 1    #아무곳이나 해도 상관없음
    #     traverse(L[v])
    #     traverse(R[v])
    #
    # traverse(N)
    # print(ans)

    # 함수 리턴해서 만들고 싶을때
    # def traverse(v):
    #     if v == 0: return 0
    #     l = traverse(L[v])
    #     r = traverse(R[v])
    #
    #     return l + r + 1
    #
    # print(traverse(N))

    #스택이용
    ans = 0
    Q = [N]
    while Q:
        v = Q.pop(0)
        if v == 0: continue
        ans += 1
        Q.append(L[v])
        Q.append(R[v])

    print(ans)