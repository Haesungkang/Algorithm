import sys
sys.stdin = open('sample_input.txt', 'r')

def merge(a):
    global cnt
    if len(a) == 1:
        return a
    else:
        m = len(a) // 2 #분할의 기준
        left = a[:m]
        right = a[m:]

        # 재귀호출 -> 기준대로 나눠버리기
        left = merge(left)
        right = merge(right)

        idxl = 0
        idxr = 0
        i = 0  # 원배열에 접근할 인덱스
        # 왼, 오 자료를 순회할 동안 반복
        while idxl < len(left) and idxr < len(right):
            if left[idxl] < right[idxr]:
                a[i] = left[idxl]
                idxl += 1
            else:
                a[i] = right[idxr]
                idxr += 1
            i += 1
        # 한쪽이 탐색이 끝나도 위의 반복을 종료
        if left[-1] > right[-1]:
            cnt = cnt + 1
        if idxl < len(left): # 왼쪽이 남음
            a[i:] = left[idxl:]
        if idxr < len(right): # 오른쪽이 남음
            a[i:] = right[idxr:]
    return a



T = int(input())
for tc in range(1, T+1):

    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    A = merge(A)
    print("#{} {} {}".format(tc, A[N // 2],cnt))