arr = [1,2,3]
#for문을 하나씩 쓰면서 확인해보기
N =len(arr)
#그냥이대로 진행했을경우 변경했을경우에서 다시 변경되는것이기때문에 주의하자

for i in range(0, N):
    arr[0], arr[i] = arr[i], arr[0]

    for j in range(1, N):
        arr[1], arr[j] = arr[j], arr[1]

        for k in range(2, N):
            arr[2], arr[k] = arr[k], arr[2]
            print(arr)
            arr[2], arr[k] = arr[k], arr[2]

        arr[1], arr[j] = arr[j], arr[1]
    # 다시 초기화시키다
    arr[0], arr[i] = arr[i], arr[0]

# 위에 있는 방식을 재귀를 이용해서 풀이하는 방법
arr = [1,2,3]

def perm(k):
    if k == N:
        print(arr)
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k+1)
            arr[k], arr[i] = arr[i], arr[k]
perm(0)