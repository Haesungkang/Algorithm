import sys
sys.stdin = open("sample_input_2.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())
    T = [0] * (N+1)

    cnt = 1
    def inorder(v):
        global cnt
        if v > N: return

        inorder(v*2)
        T[v] = cnt
        cnt += 1
        inorder(v*2+1)

    inorder(1)
    print(T[1], T[N//2])

