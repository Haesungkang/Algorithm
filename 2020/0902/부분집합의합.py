# 부분집합의 합이 10인 부분집합의 개수 찾기( +@ : 부분집합 출력)
# 부분집합(재귀,완전탐색)

# 교수님의 해설필요
N = 10  # 1~N: 원소의 집합
K = 10  # 부분집합의합

def subset(k, sum):

    if k == N:
        for i in range(N):
            if bit[i] == 1:
                sum += arr[i]
        if sum == 10:
            
        return

    bit[k] = 0
    subset(k+1, sum)
    bit[k] = 1
    subset(k+1, sum)

arr = [1,2,3]
N = len(arr)
bit = [0] * N