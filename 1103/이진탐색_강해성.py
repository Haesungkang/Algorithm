import sys
sys.stdin = open('sample_input_1.txt', 'r')

def search(number, l, r):
    global cnt, lr

    mid = (l + r) // 2
    # if arrN[mid] == l or arrN[mid] == r:
    #     if lr == [True, True]:
    #         cnt += 1
    #         return

    if arrN[mid] == number:
        cnt += 1
        return

    elif arrN[mid] < number:
        if lr[1]:
            return
        lr[1] = True
        search(number, mid+1, r)
    else:
        if lr[0]:
            return
        lr[0] = True
        search(number, l, mid-1)

    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 참조하는 idx
    arrN = sorted(list(map(int, input().split())))
    Z = len(arrN)
    # 하나씩 꺼내는 배열
    arrF = sorted(list(map(int, input().split())))
    cnt = 0
    lr = [False, False]
    for i in arrF:
        if i < min(arrN) or i > max(arrN): continue
        lr = [False, False]
        search(i, 0, Z-1)

    print("#{} {}".format(tc, cnt))

    #print(N, M, arrN, arrM)
