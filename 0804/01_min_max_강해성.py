import sys
sys.stdin = open('input.txt', 'r')

# TestCase input
T = int(input())

# 각각의 TC를 조사
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    #초기 min max 설정
    maxnumber = arr[0]
    minnumber = arr[0]
    # for구문을 통해 min,max 조사
    for i in range(0, len(arr)):
        if maxnumber < arr[i]:
            maxnumber = arr[i]
        if minnumber > arr[i]:
            minnumber = arr[i]
    #output설정
    final = maxnumber - minnumber
    print('#{} {}'.format(tc, final))





