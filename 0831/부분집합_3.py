arr = [1,2,3]
N = len(arr)
A = [0] * N # 원소의 포함여부 저장

def powerset(n, k): # n: 원소의 갯수, k : 현재 depth
    if n == k:      # basis part
        print(A, end= " ")
        for i in range(n):  #각 부분 배열의 원소 출력
            if A[i] == 1:   #A[i]가 1이면 포함된것이므로 출력
                print(arr[i], end=" ")
        print()
    else:
        #Inductive Part
        #k번째 선택
        A[k] = 1 # 다음 요소 포함여부 결정
        powerset(n, k+1)
        #k번째 비선택
        A[k] = 0 # 다음 요소 포함여부 결정
        powerset(n, k+1)

powerset(N, 0)