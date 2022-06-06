import sys

sys.stdin = open('./2022/0601/inputfolder/input6.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    #print(N, arr)
    A = True
    answer = 0
    B = 0
    for j in range(len(arr)):
        if arr[j] == 1:
            B = j
            break
    while A:
        for i in range(len(arr)):
            if arr[i] == 1:
                answer += 1
                N -= 1
            else: 
                answer += 1  
                #print(N)
            if  N == 0:
                A = False
                break
    
    print("#{} {}".format(tc, answer-B))
