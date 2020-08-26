import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    T = int(input())
    ladder = [ list(map(int, input().split())) for _ in range(100)]
    # print(ladder)
    ans_idx = 0
    for ans in range(100):
        if ladder[99][ans] == 2:
            ans_idx = ans
    i = 99
    j = ans_idx
    while i > 0:
        if j > 0 and ladder[i][j-1] == 1:
            j -= 1
            ladder[i][j] = 0
        elif j < 99 and ladder[i][j+1] == 1:
            j += 1
            ladder[i][j] = 0
        else:
            i -= 1
            ladder[i][j] = 0
    print("#{} {}".format(tc, j))
