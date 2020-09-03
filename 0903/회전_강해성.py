import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(input().split())

    for i in range(M):
        queue = arr.pop(0)
        arr.append(queue)

    print("#{} {}".format(tc, arr[0]))