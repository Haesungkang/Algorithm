arr = [1,2,3,4,5]
'''
부분집합을 출력하는 코드 작성
비트마스킹을 이용해서
'''

N = len(arr)
for i in range(1 << N):
    for j in range(N):
        if i & (1<< j):
            print(arr[j], end=' ')
    print()
print()