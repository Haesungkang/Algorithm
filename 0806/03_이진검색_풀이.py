def binarySearch(s, e, key):
    l, r = s, e
    cnt = 0
    while l <= r:
        mid = int((l+r) / 2)
        cnt += 1
        if key == mid:
            break
        elif key < mid:
            r = mid
        else:
            l = mid
    return cnt
# 문제에서 요구하는 방법은 오류가 생길수있다
# mid에서 +1을 안하는 경우
# 이진탐색에서는 왼쪽에서 오른쪽에서 +1 -1을 무조건해야한다


