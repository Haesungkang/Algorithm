N, K = map(int,input().split())

# arr = [i for i in range(1, 12+1)]
ans = 0
for bits in range(1, 1 << 12):
    cnt = S = 0
    for i in range(12): # i = 0~11
        if bits & (1 << i):
            cnt += 1
            # S += arr[i]
            S += i + # (1~12)

    if cnt == N and S == K:
        ans += 1