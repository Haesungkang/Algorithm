import sys
sys.stdin = open('input6.txt', 'r') # 파일로 인풋받기

for tc in range(1, 11):

    T = int(input())
    mylist = [list(map(int, input().split())) for _ in range(100)]
    sumlist = []
    #가로
    for i in mylist:
        sumlist.append(sum(i))
    #세로
    for j in range(100):
        sumlist2 = 0
        for i in range(100):
            sumlist2 += mylist[i][j]
        sumlist.append(sumlist2)
    #대각선
    sum3 =0
    for i in range(100):
        sum3 += mylist[i][i]
    sumlist.append(sum3)
    #대각선2
    sum4 = 0
    for i in range(0, 100):
        sum4 += mylist[i][99-i]
    sumlist.append(sum4)
    #모든경우의 수에서 max찾기
    maximum = max(sumlist)
    print('#{} {}'.format(T, maximum))
