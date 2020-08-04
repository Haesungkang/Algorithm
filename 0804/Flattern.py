import sys
sys.stdin = open('input5.txt', 'r')

for tc in range(1, 11):
    Dump = int(input())
    arr = list(map(int, input().split()))

    for j in range(0, Dump):
        maximum = max(arr)
        minimum = min(arr)
        for i in range(0, len(arr)):
            if arr[i] == maximum:
                arr[i] -= 1
                break
        for i in range(0, len(arr)):
            if arr[i] == minimum:
                arr[i] += 1
                break
    final = max(arr) - min(arr)
    print('#{} {}'.format(tc, final))

