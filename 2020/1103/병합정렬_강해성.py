import sys
sys.stdin = open('sample_input.txt', 'r')

def merge(left, right):
    result = []
    #print(left, right)
    global rightpoint
    while len(left) > 0 or len(right) > 0 :
        if len(left) > 0 and len(right) > 0 :
            if left[0] >= right[0]:
                result.append(left.pop(0))
                rightpoint += 1
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0 :
            result.append(right.pop(0))
    #print(rightpoint)
    return result

#분할과정
def merge_sort(arr):
    #print(arr)
    if len(arr) == 1:
        return arr
    left = []
    right =[]
    mid = len(arr)//2
    for i in range(len(arr)):
        if i < mid :
            left.append(arr[i])
        else:
            right.append(arr[i])

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)


T = int(input())
for tc in range(1, T+1):
    rightpoint = 0
    N = int(input())
    arr = list(map(int, input().split()))
    arr_result = merge_sort(arr)
    print("#{} {} {}".format(tc, arr_result[N//2], rightpoint))