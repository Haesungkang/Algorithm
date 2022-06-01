def seq_search(a, n, k):
    i = 0
    while i < n and a[i] != k:
        i += 1
    if i < n: return i
    else: return -1

arr = [4, 9, 11, 23, 2, 19, 7]
key = 2
print(seq_search(arr, len(arr), key))

# def seq_search(a, n, k):
# #     i = 0
# #     while i < n and a[i] < key:
# #         i += 1
# #     if i < n and a[i] == key: return i
# #     else: return -1
# 정렬되어있는경우