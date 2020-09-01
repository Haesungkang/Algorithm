import sys
sys.stdin = open("input.txt", "r")

def move(arr, N):
    for j in range(N):
        for i in range(N):
            if arr[i][j] == 1:
                if i == 99:
                    arr[i][j] = 0
                elif arr[i + 1][j] == 0:
                    arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

            if arr[i][j] == 2:
                if i == 0:
                    arr[i][j] = 0
                elif arr[i - 1][j] == 0:
                    arr[i][j], arr[i - 1][j] = arr[i - 1][j], arr[i][j]

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    rb_list = []
    for t in range(100):
        move(arr, N)
    result = 0
    for j in range(N):
        for i in range(N-1):
            if arr[i][j] == 1:
                if arr[i+1][j] ==2:
                    result += 1
    print("#{} {}".format(tc, result))