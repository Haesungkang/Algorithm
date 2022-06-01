def bin_search(a,key):
    start = 0
    end = len(a)-1
    while start <= end:
        middle = (start + end) // 2
        # ==
        if a[middle] == key:
            return True, middle  # python의 경우 tuple의 값으로 넘길수있다
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
        # <
        # >
    return False, -1



arr = [2, 4, 7, 9, 11, 19, 23]
key = 7
print(bin_search(arr, key))
