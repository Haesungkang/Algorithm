import sys
sys.stdin = open('sample_input_4.txt', 'r')

def search(i):
    global counting
    if arr[i][1] == 24:
        return
    for j in range(len(arr)):
        if arr[i][1] <= arr[j][0] and visited[j] == 0:
            counting += 1
            visited[j] = 1
            search(j)

    # if arr[i][1] == 24:
    return counting


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    reserv = []
    for i in range(N):
        S, E = map(int, input().split())
        reserv.append([S,E])

    arr = sorted(reserv)
    visited= [0] * len(arr)
    countinglist = []
    for i in range(len(reserv)):
        visited = [0] * len(arr)
        counting = 1
        search(i)
        countinglist.append(counting)
    print(countinglist)