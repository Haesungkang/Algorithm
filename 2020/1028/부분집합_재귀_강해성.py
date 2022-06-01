'''
부분집합 : 재귀를 이용해서
'''
def subset(k):
    if k == N:
        for i in range(N):
            if bit[i] == 1:
                print(arr[i], end=' ')
        print()
        return
    else:
        bit[k] = 0
        subset(k+1)
        bit[k] = 1
        subset(k+1)




arr = [1,2,3,4,5]
N = len(arr)
bit = [0] * (len(arr))
subset(0)
