
def subset(n, k):
    if n == N:
        #출력
        for i in range(N):
            if bit[i]:
                print(arr[i], end=" ")
        print()

    # 선택, 비선택
    bit[n] = 0
    subset(n+1, k) #k는 선택한 원소수
    bit[n] = 1
    subset(n+1, k+1)


arr = [1,2,3]  # 선택할 원소 모인 배열
N = len(arr)
bit = [0] * N  # 원소선택여부 저장
subset(0)       # 부분집합 함수 호출 -> 이렇게 4줄쓴다음에 def로 넘어가서 함수작성

