# 10분동안 부분집합 구현하기 - 재귀
def subset(k):   #현재 선택할지 말지 결정할 원소의 위치
    # 재귀 : 종료조건을 설정해야한다
    #여기부분을 채워서 부분집합 구현(출력)
    if k == N:
        #출력하고 끝
        print(bit)
        for i in range(N):
            if bit[i] == 1:
                print(arr[i], end=' ')
        print()
        return
    #현재위치의 원소 선택할지 말지 결정하고, 다음 원소로 넘어감
    bit[k] = 0
    subset(k+1)
    bit[k] = 1
    subset(k+1)


arr = [1,2,3]   #선택할 원소
N = len(arr)    #원소의 개수
bit = [0] * N
#원소선택 여부 저장
subset(0)
