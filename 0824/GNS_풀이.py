import sys
sys.stdin = open('../0inputlist/GNS_test_input.txt','r')
#GNS
T = int(input())
for tc in range(1,T+1):
    t,N = input().split()
    N = int(N)
    # print(N)
    #리스트에 문자열을 저장
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    counts = [0 for i in range(10)] #수를 카운팅하기 위한 배열
    arr = input().split()            #입력을 받아서 배열에 저장
    # print(N)
    # print(arr)
    for i in range(len(arr)):
        for j in range(len(nums)):
            if arr[i] == nums[j]:   #입력받은 배열에서 하나꺼내서 비교리스트와 비교하고 카운팅하기
                counts[j] += 1
    # print(counts)
    print(t)
    for i in range(len(counts)):
        for j in range(counts[i]):
            print(nums[i], end=" ")
    print()
