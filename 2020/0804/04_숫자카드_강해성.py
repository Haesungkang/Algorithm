import sys
sys.stdin = open('input4.txt', 'r') # 파일로 인풋받기

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    arr = list(map(int, input()))
    # Maximum 값 찾기
    maxi = 0
    for m in arr:
        if maxi < m:
            maxi = m
    # dict으로 표현하기
    list2 = dict()
    for i in range(len(arr)):
        counting = arr.count(arr[i])
        list2[arr[i]] = counting
    print(list2)
    # 최빈값 찾기
    counting2 = 0
    for key, value in list2.items():
        if value > counting2:
            counting2 = value
    # 최빈값들끼리 리스트 만들기
    list3 = dict()
    for key, value in list2.items():
        if counting2 == value:
            list3[key] = value
    # 최빈값중 가장 큰값 찾아내기
    best = 0
    for key, value in list3.items():
        if key >= best:
            best = key

    for key, value in list3.items():
        if best == key:
            print('#{} {} {}'.format(tc, key, value))

    # 오류과정

    # maxvalue = 0
    # for key, value in list3.items():
    #     if key > maxvalue:
    #         maxvalue = {key : value}
    #
    # print(maxvalue)

    # print(list2)
    # print(maxi)
    # counting2 = 0
    # for key, value in list2.items():
    #     if value > counting2:
    #         counting2 = value
    #
    # for key, value in list2.items():
    #     if list2[maxi] == counting2 and counting2 == value:
    #         print('#{} {} {}'.format(tc, maxi, counting2))
    #         break
    #     if list2[maxi] != counting2 and counting2 == value:
    #         print('#{} {} {}'.format(tc, key, value))






