import sys
sys.stdin = open("sample_input.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sel = len(arr) * [0]
    result = set()

    def comb(n, r, N):
        if r == N:
            result.add(sum(sel))
            return
        elif n >= len(arr):
            return
        sel[r] = arr[n]
        comb(n + 1, r + 1, N)
        comb(n + 1, r, N)

    for i in range(N):
        comb(0,0,i)

    print("#{} {}".format(tc, len(result)+1))