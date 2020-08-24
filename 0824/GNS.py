import sys
sys.stdin = open('../0inputlist/GNS_test_input.txt', 'r')

T  = int(input())
for tc in range(1, T+1):
    N = input().split()
    arr = list(input().split())
    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(len(arr)):
        for j in range(10):
            if arr[i] == num_list[j]:
                arr[i] = j
    finalarr = sorted(arr)
    for i in range(len(finalarr)):
        for j in range(10):
            if finalarr[i] == j:
                finalarr[i] = num_list[j]
    arrr = ' '.join(finalarr)
    print("#{}".format(tc))
    print("{}".format(arrr))
