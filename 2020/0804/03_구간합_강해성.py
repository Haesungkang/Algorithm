
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # minmax의 초기값을 설정합니다
    minlist = arr[0:0+M]
    min = 0
    max = 0
    for i in minlist:
        min += i
        max += i
    #구간을 쪼개서 각각의 합을 구합니다
    for j in range(0, N-M+1):
        compare = arr[j:M+j]
        com = 0
    # min, max값을 찾아줍니다
        for j in compare:
            com += j
        if  max <= com:
            max = com
        if  min >= com:
            min = com

    final = max - min
    print('#{} {}'.format(tc, final))




