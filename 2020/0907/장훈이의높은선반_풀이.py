import sys
sys.stdin = open("input.txt", "r")

def calc(cursum):   # B를 넘는 탑의 높이중 최소값 찾기
    global ans
    if cursum >= B:
        if ans > cursum:
            ans = cursum

def powerset(k, cursum):
    if ans < cursum: return # 가지치기
    #n: 점원수(k랑 비교해서 같아지면 끝내기위한 것)
    # cursum: 키의 합
    if k == N: #선택여부를 다 결정하면
        calc(cursum)
    else:
        #A[k] = 1
        powerset(k+1, cursum+h[k]) # k번째 원소 선택함, cursum에 더해줌
        #A[k] = 0
        powerset(k+1, cursum)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())    # 점원수, 선반높이
    h = list(map(int, input().split())) # 점원의 키들
    ans = 0xffffff # 큰값을 초기설정
    A = [0] * N #원소 선택여부 저장
    powerset(0, 0)  # 부분집합구하기
    print("#{} {}".format(tc, ans-B))