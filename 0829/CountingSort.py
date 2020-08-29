def Counting_Sort(A, K):
    # 입력배열 A[1...n]
    # 정렬된배열 B[1...n]
    # 카운트배열 C[1....n]
    B = [0] * len(A)
    C = [0] * (K+1)

    for i in range(len(B)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    # for i in range(len(B)-1, -1, -1):
    #     B[C[A[i]] - 1] = A[i]
    #     C[A[i]] -= 1

    for i in reversed(range(len(A))):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

    return B

A=[2,0,2,0,4,1,5,5,2,0,2,4,0,4,0,3]
print(Counting_Sort(A, 5))
