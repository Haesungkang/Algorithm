import sys
sys.stdin = open("sample_input_2.txt", "r")

def check(oven, oven_idx):
    C = oven.pop(0)
    idx = oven_idx.pop(0)
    if C == 0:
        if arr:
            oven.insert(0, arr.pop(0))
            oven_idx.insert(0, arr_idx.pop(0))
    else:
        half = C // 2
        oven.append(half)
        oven_idx.append(idx)
    # print(oven)
    # print(oven_idx)
    # print()

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_idx = list(i for i in range(M))
    # 오븐생성
    oven = []
    for i in range(N):
        oven.append(arr.pop(0))
    # 오븐 인덱스생성
    oven_idx = []
    for i in range(N):
        oven_idx.append(arr_idx.pop(0))

    #오븐 안에서 체크하기
    while len(oven) > 1:
        check(oven, oven_idx)

    print("#{} {}".format(tc, (oven_idx[0]+1)))

