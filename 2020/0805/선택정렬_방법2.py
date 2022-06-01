def selection(a, k):
    # i : 0 ~ len(n) -1
    for i in range(k):   # 0, 1, 2, 3
        # 최소값 찾기
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]: # 여기바꿔주면 내림차순 오름차순 바꿀수있다
                min = j
        a[i], a[min] = a[min], a[i]
    return a[k-1]

arr = [64, 25, 10, 22, 11]

print(arr)
print(selection(arr,3))