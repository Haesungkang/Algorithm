'''
합병 정렬

1. 자료를 최소단위(1개) 까지 쪼갬

'''
def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0: # 배열이 자료가 있는동안 반복
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0: # 왼쪽 자료가 있는 경우
            result.append(left.pop(0))
        elif len(right) > 0: # 오른쪽 배열자료가 있는경우
            result.append(right.pop(0))
    return result



# 분할과정
def merge_sort(arr):
    # print(arr)
    if len(arr) == 1:
        return arr
    left = []  # 왼쪽배열
    right = [] # 오른쪽배열
    mid = len(arr)//2 # 절반으로 자르기위한 변수
    for i in range(len(arr)):
        if i < mid:
            left.append(arr[i])
        else:
            right.append(arr[i])
    left = merge_sort(left) # 왼쪽에 대해서 분할 -> 재귀
    #리턴된자리
    right = merge_sort(right) # 오른쪽에 대해서 분할 -> 재귀
    return merge(left,right)


arr = [69,10,30,2,16,8,31,22]
arr_result = merge_sort(arr)
print(arr_result)