import sys
sys.stdin = open("sample_input_3.txt", "r")

def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount
    parent = cur // 2

    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2

for tc in range(1, int(input())+1):
    N = int(input())
    temp = list(map(int, input().split()))
    heapcount = 0
    heap = [0] * (N+1)
    for i in range(N):
        heappush(temp[i])

    #print(heap)
    result = 0
    idx = N
    while idx >= 1:
        idx = idx // 2
        result += heap[idx]

    print("#{} {}".format(tc, result))

