# 최소힙

def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount
    parent = cur // 2

    # 루트가 아니고, if 부모노드값 > 자식노드값 -> swap을 해야한다
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        # cur 갱신해서 밑에 parent도 갱신
        cur = parent
        parent = cur // 2

def heappop():
    global heapcount
    retValue = heap[1]
    # heapcount맨마지막 같을 넣고 시작한다
    heap[1] = heap[heapcount]
    # 빼낸거 지우겠다
    heap[heapcount] = 0
    heapcount -= 1

    parent = 1
    child = parent * 2

    if child + 1 <= heapcount: # 오른쪽 자식 존재
        # 왼쪽오른쪽을 비교한다
        if heap[child] > heap[child+1]:
            child = child +1
    # 자식노드가 존재하고, 부모노드 > 자식노드 -> swap
    while child <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heapcount:  # 오른쪽 자식 존재
            # 왼쪽오른쪽을 비교한다
            if heap[child] > heap[child + 1]:
                child = child + 1
    return retValue

#heapcount를 해야지 몇개를 차지하고있는가를 알수있다
heapcount = 0
temp = [7, 2, 5, 3, 4, 6]
N = len(temp)
heap = [0] * (N+1)
for i in range(N):
    heappush(temp[i])

for i in range(N):
    print(heappop(), end=" ")
print()