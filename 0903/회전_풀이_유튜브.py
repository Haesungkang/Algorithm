import sys
sys.stdin = open("sample_input.txt", "r")

# 1. pop(0),append이용  2. M%N이용  3. 선형큐이용
# 4. 원형큐 -> 원형큐에서는 한개공간이 더있어야한다

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())     # M은 최대 1000
    Q = list(map(int, input().split()))

    #원형큐이용
        # Q = [0] + list(map(int, input().split()))
        # f, r = 0, N
        # Size = N + 1
        # for _ in range(M):
        #     f = (f+1) % Size
        #     r = (r+1) % Size
        #     Q[r] = Q[f]
        # print(Q[(f+1)%Size])

    #선형 큐이용
        # Q = Q + ([0] * M)
        # f, r = -1, N-1
        #
        # for _ in range(M):
        #     f += 1 #Q[f]
        #     r += 1
        #     Q[r] = Q[f]
        #
        # print(Q[f + 1])

    #pop & append이용
        # for _ in range(M):
        #     Q.append(Q.pop(0))
        # print(Q[0])


    #나머지 이용
        # print(Q[M%N])





