import sys
sys.stdin = open("input.txt", "r")

def subset(k, sum):
    global result, S, mini
    if k == N:
        for i in range(N):
            if bit[i] == 1:
                sum += arr[i]
        result = sum - S
        if result >= 0 and mini > result:
            mini = result
        return
    else:
        bit[k] = 0
        subset(k+1, sum)
        bit[k] = 1
        subset(k+1, sum)

T = int(input())
for tc in range(1, T+1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    length = len(arr)
    result=[]
    mini = 99999
    bit = [0] * length
    subset(0,0)
    print("#{} {}".format(tc, mini))
