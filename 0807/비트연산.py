# 4bit --> 0~15
# 4bit로 표현 가능한 모든 경우 중에 1이 2번 포함된 경우
# 1100, 1010, 1001
arr = [1, 2, 3, 4]

for bits in range(1 << 4):
    cnt = 0
    for i in range(4):
        if bits & (1 << i):
            cnt += 1
            S += arr[i]

    if cnt == 2 and S == 10:
        for i in range(3, -1, -1):
            if bits & (1 << i): print(1, end="")
            else: print(0, end='')
        print()