import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(idx, result):   # 몇번째 연산자 고르는지 : id, 현재까지의 연산결과 : result
    global minV, maxV
    if idx  == N-1: # 연산자 다고름
        # 최대값 최소값 찾기
        if maxV < result:
            maxV = result
        if minV > result:
            minV = result
        return
    #연산자 선택지
    for i in range(4):
        if op[i] > 0:   # 연산자 카드가 있을때만 고려하기
            op[i] -= 1  # 연산자 카드 사용
            if i == 0:  # 연산자 +
                temp = result + num[idx+1] #현재까지의 결과 + 다음카드
            elif i == 1: #연산자 -
                temp = result - num[idx+1]
            elif i == 2:  # 연산자 -
                temp = result * num[idx + 1]
            else:
                temp = int(result / num[idx + 1])
            dfs(idx+1, temp)
            op[i] += 1 #연산자 취소 시키는 작업


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    op = list(map(int, input().split()))
    num = list(map(int, input().split()))
    maxV = -999999
    minV = 9999999
    #연산값, 숫자idx, 결과값 등을 들어가고 시작한다는 마인드
    dfs(0, num[0]) # 연산자의 위치, 피연산자의 시점
    print("#{} {}".format(tc, maxV-minV))