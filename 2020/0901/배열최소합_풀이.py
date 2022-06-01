import sys
sys.stdin = open("sample_input_4.txt", "r")

# 먼저 설계를 한다 -> 경우의 수를 파악하면서
# 기본적으로 손으로 test를 해본다/ 작은크기로
# 순열  # 총합->최소값 # 백트래킹, min값보다 커버리면안해도되는것

def find(n,s): #n : 현재행, s: 총합
    global minV
    if n == N: # 순열을 완성하면
        #순열에 해당하는 값을 더하고, 최소값인지 판단
        if s < minV: #지역변수가 아니라 전역변수임을 확인하기위해서
            minV = s
        return
    # 지금 들어있는 s의 값이 최소값보다 클경우는 더이상진행하지않기 위함
    elif minV <= s: #백트래킹, 순열완성이 완성되지 않았지만 이미 최소가 아닌경우
        return
    else:
        for i in range(N):
            if u[i] == 0 : #아직 선택되지 않았다면
                u[i] = 1
                find(n+1, s + arr[n][i]) #s라는 누적합에서 추가시킨다
                u[i] = 0 #선택취소


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    u = [0 for _ in range(N)] #*N은 조심하기 #방문배열
    minV = 10000
    # 0행에서 시작, 총합 : 0
    find(0,0) #현재 행(perm(K)를 의미 #sum값을 넣는 느낌
    print("#{} {}".format(tc, minV))
