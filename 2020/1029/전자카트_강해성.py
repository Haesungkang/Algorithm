import sys
sys.stdin = open('sample_input_1.txt', 'r')


def perm(k):
    global finalresult
    if k == N-1:
        #print(sel)
        result = 0
        for i in range(len(sel)):
            if i == 0:
                result += arr2[0][sel[i]]
                result += arr2[sel[i]][sel[i+1]]
            elif i == len(sel)-1:
                result += arr2[sel[len(sel)-1]][0]
            else:
                result += arr2[sel[i]][sel[i+1]]
        finalresult.append(result)
        return
    for i in range(N-1):
        if visited[i] == 0:
            sel[k] = arr[i]
            visited[i] = 1
            perm(k + 1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr2 = [list(map(int, input().split())) for _ in range(N)]

    arr = []
    for i in range(N-1):
        arr.append(i+1)
    #print(arr)
    sel = [0] * (N-1)
    visited = [0] * (N-1)  # 원소 선택여부 저장
    result = 0
    finalresult = []
    perm(0)
    print("#{} {}".format(tc, min(finalresult)))