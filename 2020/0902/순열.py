def perm(n, k):
    # 만약에 순열문제를 푼다면 여기서 제대로 나온다음에 추가로 붙이는게 좋다고 생각한다
    if k == n:
        print(arr)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]

arr = [1,2,3]
N = len(arr)
perm(N, 0)