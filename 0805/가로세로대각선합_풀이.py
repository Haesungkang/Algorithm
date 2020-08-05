import sys
sys.stdin = open('../0inputlist/input6.txt', 'r')

T = 10
N = 100

for _ in range(1, T+1):
    tc = int(input()) #테케번호 입력받기
    arr = [list(map(int, input().split())) for _ in range(N)] #한줄배열을 잡고 그다음에 range시키는느낌
    max = 0 # 최대값을 저장하기 위한 변수
    for i in range(N):
        sum = 0 #누적합 저장
        for j in range(N):
            sum += arr[i][j]
        if max < sum:
            max = sum
        #print(sum)
    #열반복 : 0,0 -> 1.0 -> 2,0
    for j in range(N):
        sum = 0
        for i in range(N):
            sum += arr[i][j]
        if max < sum:
            max = sum
    #대각선 반복 : 1,1 -> 2,2 -> 3,3
    sum = 0
    for i in range(N):
        sum += arr[i][i]
    if max < sum:
        max = sum
    #역대각선
    sum = 0
    for i in range(N):
        sum += arr[i][N-i-1]
    if max < sum:
        max = sum



    print("#{} {}".format(tc, max))


