import sys
sys.stdin = open("sample_input_1.txt", "r")

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    T = [0] * (N+1)
    for _ in range(M):
        num, val = map(int, input().split())
        T[num] = val

    # def dfs(v):
    #     if v > N: return 0
    #     l = dfs(v*2)
    #     r = dfs(v*2 +1)
    #     T[v] += l + r
    #
    #     return T[v]
    # dfs(1)

    for i in range(N-M, 0, -1):     #배열의 인덱스아자, 노드번호
        T[i] = T[i*2] + T[i*2+1]
        if i*2 + 1 <= N:
            T[i] += T[i*2+1]

    print(T[L])