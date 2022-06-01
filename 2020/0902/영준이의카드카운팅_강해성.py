import sys
sys.stdin = open("sample_input.txt", "r")

def check(arr, String):
    idx = [0] * 14
    for i in range(len(arr)//3):
        number = 0
        if arr[3*i] == String:
            number += 10* int(arr[3*i+1])
            number += int(arr[3*i+2])
            idx[number] += 1

    result = 13
    for i in range(len(idx)):
        if idx[i] > 1:
            return -1
        else:
            result -= idx[i]
    return result

T = int(input())

for tc in range(1, T+1):
    T = input()
    arr = []
    for text in T:
        arr.append(text)

    if check(arr, 'S') > 0 and check(arr, 'D') > 0 and check(arr, 'H') > 0 and check(arr, 'C') > 0:
        print("#{} {} {} {} {}".format(tc, check(arr, 'S'), check(arr, 'D'), check(arr, 'H'), check(arr, 'C')))
    else:
        print("#{} ERROR".format(tc))


