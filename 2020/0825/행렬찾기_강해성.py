import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    list1=[]
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            garo = 1
            sero = 1
            #while문을 이용해서 가로세로의 길이를 측정합니다
            if arr[i][j] != 0:
                while arr[i][j+garo] != 0:
                    garo +=1
                while arr[sero+i][j] != 0:
                    sero +=1
                #이미 측정한 값들은 다시 blank처리를 해줍니다
                for blank1 in range(sero+1):
                    for blank2 in range(garo+1):
                        arr[i+blank1][j+blank2] = 0
                list1.append([sero, garo])
    multilist = []
    #리스트를 제작한것을 다시 순서대로 작성하기위한 코드
    #크기 순서대로작성
    for i in list1:
        multi = 1
        for j in i:
            multi *= j
        multilist.append(multi)
    for i in range(len(multilist)-1):
        min = i
        for j in range(i+1, len(multilist)):
            if multilist[min] > multilist[j]:
                min = j
        list1[i], list1[min] = list1[min], list1[i]
    #크기가 동일한것에 대한 행순서로 변경
    for i in range(len(multilist) - 1):
        min = i
        for j in range(i + 1, len(multilist)):
            if multilist[min] == multilist[j]:
                if list1[min][0] > list1[j][0]:
                    min = j
        list1[i], list1[min] = list1[min], list1[i]
    #프린트하기
    print("#{} {}".format(tc, len(list1)), end=" ")
    for i in list1:
        for j in i:
            print(j, end=" ")
    print()
