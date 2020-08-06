import sys
sys.stdin = open('input7.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())
    #기본값 설정
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    length = len(arr)
    #부분집합을 만드는 함수를 제작합니다
    findsum = 0
    for i in range(1<<length):
        list2 =[]
        for j in range(length):
            if i & (1 << j):
                list2.append(arr[j])
        # 부분집합중에서 개수와 합이 맞는것을 카운트합니다
        if len(list2) == N and sum(list2) == K:
            findsum +=1

    print("#{} {}".format(tc, findsum))
