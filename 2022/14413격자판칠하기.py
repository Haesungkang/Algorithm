# bfs로 접근해야되는게 아니라 set이나 홀수 짝수로 판단해야하는 문제
import sys
sys.stdin = open('./2022/inputfolder/14413.txt', 'r')

dc, dr = [0,0,-1,1], [1,-1,0,0]
T = int(input())
def check(i, j):
    checklist = []
    for x in range(4):
        nc = i + dc[x]
        nr = j + dr[x]
        if nc < 0 or nc >= N or nr < 0 or nr >= M:
            continue
        if arr[i][j] == "#":
            if arr[nc][nr] == "#":
                return False
        if arr[i][j] == ".":
            if arr[nc][nr] == ".":
                return False
        if arr[nc][nr] == "#" or "." or "?":
            checklist.append(arr[nc][nr])
    #print(checklist)
    if '#' in checklist and "." in checklist:
        return False
    return True

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = []
    for i in range(N):
        arr.append(list(input()))
    #print(arr)
    result = True
    cnt = 0

    for i in range(N):
        for j in range(M):
            if not check(i, j):
                cnt += 1

    if cnt > 0 :
        print("#{} impossible".format(tc))   
    else:
        print("#{} possible".format(tc)) 
    
