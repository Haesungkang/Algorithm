#순열 n개의 원소중에서 r개를 뽑아서 나열한 곳

def perm(k): #k : 선택할 원소가 들어갈 위치 (sel)
    global result
    if k == N: # 선택 끝! (sel 완성)
        result.append(sel[:])
        # A 0번에 있는거 b 0 번에 넣는거
        # A[0] = B[0]
        # A[1] = B[1]
        '''
        for i in range(N):
            A[i] = B[i]
        '''
        # different language => use for구문
    for i in range(N):
        if visited[i] == 0:
            sel[k] = arr[i]
            visited[i] = 1
            perm(k+1)
            visited[i] = 0


arr = [1,2,3]
N = len(arr)
result = []
sel = [0] * N # 생성할 순열을 저장할 배열
visited = [0] * N # 원소 선택여부 저장
perm(0)
print(result)
