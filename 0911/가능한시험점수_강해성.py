import sys
sys.stdin = open("sample_input.txt", "r")

def subset(k):
    global result
    if k == N:
        number = 0
        for index, value in enumerate(bit):
            if value == 1:
               number += arr[index]
        result.add(number)
        return
    bit[k] = 0
    subset(k+1)
    bit[k] = 1
    subset(k+1)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    bit = len(arr) * [0]
    result = set()
    subset(0)
    print("#{} {}".format(tc, len(result)))