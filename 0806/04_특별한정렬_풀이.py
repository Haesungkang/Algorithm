# 선택정렬
arr = [64,25,10,22,11]
N = len(arr)

for i in range(0, N-1): # 최소 10개의 자료만 주니깐 여기를 10으로 바꾸고 출력하면된다
    idx = i # 시작 위치를 최소값 가정
    if i % 2 == 0:
        for j in range(i + 1, N):
            if arr[idx] < arr[j]:
                idx = j
    else:
        for j in range(i + 1, N):
            if arr[idx] > arr[j]:
                idx = j

    arr[i], arr[idx] = arr[idx], arr[i]

print(arr)