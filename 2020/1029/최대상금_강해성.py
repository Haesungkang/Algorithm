import sys
sys.stdin = open('input.txt', 'r')

# 한번 바꿔치기
def sorting():
    if arr == arr2:
        #print(arr)
        arr[-1], arr[-2] = arr[-2], arr[-1]
        return
    for i in range(L):
        if arr[i] != arr2[i]:
            for j in range(L-1, -1, -1):
                if arr[j] == arr2[i]:
                    arr[i], arr[j] = arr[j], arr[i]
                    break
            break
    return arr

T = int(input())
for tc in range(1, T+1):
    N, C = input().split()
    arr = list(N)
    L = len(arr)
    arr2 = sorted(list(N))[::-1]

    for i in range(int(C)):
        sorting()

    if int(C) > 1:
        idxlist = 0
        i = 0
        while i < len(arr)-1:
            if arr[i] == arr2[i + 1]:
                idxlist += 1
                i += 1
            else:
                i += 1
        if idxlist > 0:
            finalarr = arr[:L-idxlist] + sorted(arr[L-idxlist:L])[::-1]
            print("#{} {}".format(tc, ''.join(finalarr)))
        else:
            print("#{} {}".format(tc, ''.join(arr)))
    else:
        print("#{} {}".format(tc, ''.join(arr)))
    #print(arr
    # 예외처리사항
    # 이미 최대횟수가 되었는데 교환횟수가 홀수번일때
    # ['3', '2', '8', '8', '8'] 2
    # ['8', '8', '8', '3', '2']
    # ['8', '8', '8', '2', '3'] 같은 상황 처리하기

