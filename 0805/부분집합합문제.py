# 부분 집합의 합 문제 풀기
# 부분집합 구하기 -> 부분집합의 총합이 아닌 0인 부분집합이 있는지 찾기 : 교재 63page

arr = [-7,-3,-2,5,8]
N = len(arr)
sumzero =[]
for i in range(1<<N):
    list2 =[]
    for j in range(N):
        if i & (1 << j):
            list2.append(arr[j])
    if list2 != [] and sum(list2) == 0:
        sumzero = list2
        print(True)
if sumzero == []:
    print(False)


