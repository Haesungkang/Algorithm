# 최소힙
# 1차원 배열로 구현

# 삽입
def heappush(value):
    global heapcount    #마지막 위치
    heapcount += 1      #지금 들어온 원소가 저장될 위치
    heap[heapcount] = value
    cur = heapcount  # 방금 들어온 값 위치
    parent = cur // 2  # cur의 부모
    # 루트 아니고 부모노드값 > 자식노드 값 => 바꾸기
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2


# 삭제
def heappop():
    global heapcount
    retValue = heap[1]  # 루트의 값을 리턴하기위해 준비
    heap[1] = heap[heapcount]  # 루트값 <- 마지막 원소로
    heap[heapcount] = 0  # 마지막원소 지우기
    heapcount -= 1  # 힙카운트 줄이기

    parent = 1      #root부터 시작
    child = parent * 2  # 왼쪽 자식

    if child + 1 <= heapcount:  # 오른쪽 자식 존재
        if heap[child] > heap[child + 1]:
            # 오른쪽 자식 < 왼쪽자식 => 우리는 둘중에 작은 값 찾아야함
            child = child + 1  # 부모랑 비교할 자식을 오른쪽으로
    # 자식 노드가 존재하고, 부모 노드 > 자식노드 => 바꾸기
    while child <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child  # 부모 <- 자식으로 갱신
        child = parent * 2  # 현 부모의 자식을 찾기
        if child + 1 <= heapcount:  # 오른쪽 자식있으면 둘중 작은 값을 찾음
            if heap[child] > heap[child]:
                child = child + 1
    return retValue

temp = [7, 2, 5, 3, 4, 6]
N = len(temp)
heapcount = 0   #마지막으로 원소가 들어간 곳
heap = [0] * (N + 1)    #heap을 위한 배열 생성
for i in range(N):
    heappush(temp[i])
for i in range(N):
    print(heappop(), end=" ")
print()