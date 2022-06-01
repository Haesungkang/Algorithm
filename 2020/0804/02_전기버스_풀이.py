import sys
sys.stdin = open('input8.txt', 'r')

'''

정류장을 이동하면서 현 정류장을 오기위해 충전이 필요한지 아닌지 체크
- k 충전량으로 현재 정류장으로 올 수 없다면 종점을 갈 수 없으므로 0 출력하고 끝
- 마지막으로 충전 위치 저장 (last)
- 충전없이 현재 위치로 올 수 없다면 last + k  < 현위치 
    - 이전 충전기에서 충전함
    
'''
def find(v,k,n,m):
    v.insert(0,0) # insert(인덱스,데이터) : 0번인덱스에 0을 넣음
    v.append(n)   # append() : 끝에 데이터를 넣음

    last = 0 #마지막 충전했던 위치
    cnt = 0 #충전횟수
    for i in range(1,m+2):
        #   충전기 사이가 k보다 멀면 -> 종점을 못간다
        if v[i] - v[i-1] > k:
            return 0
        if v[i] > last + k:
            last = v[i-1] # 현위치 직전의 충전기에서 충전
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    #K : 한번에 충전에 갈수있는 정류장수
    #N : 종점
    #M : 충전기 설치 정류장수
    K, N, M = map(int, input().split())
    v = list(map(int, input().split()))

    print("#{} {}".format(tc, find(v,K,N,M)))



