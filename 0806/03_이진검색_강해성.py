import sys
sys.stdin = open('input9.txt', 'r')

# 원하는 페이지를 찾게 하는 이진검색 함수를 만들어줍니다
def binarysearch(page, key):
    start = 1
    end = page
    searchnum = 0
    #모든 변수 초기화시킨후 몇번찾았는지 확인합니다
    while start <= end:
        middle = int((start + end)/2)
        if middle == key:
            searchnum += 1
            return searchnum
        elif middle > key:
            end = middle
            searchnum += 1
        else:
            start = middle
            searchnum += 1
    return False

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    #각각의 값을 함수에넣어주고 그값을 비교합니다
    aresult = binarysearch(P, A)
    bresult = binarysearch(P, B)
    if aresult < bresult:
        print("#{} A".format(tc))
    elif aresult > bresult:
        print("#{} B".format(tc))
    else:
        print("#{} 0".format(tc))