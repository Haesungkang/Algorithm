# 최소힙만 지원(heapq)
import heapq
heap1 = [7,2,5,3,4,6] # list
print(heap1)
heapq.heapify(heap1)
print(heap1)

#1을 넣고 싶을때
heapq.heappush(heap1, 1)
print(heap1)

#오름차순으로 뽑아내고 싶을때
while heap1:
    print(heapq.heappop(heap1), end= " ")
print()

# 최대힙
temp = [7,2,5,3,4,6]
heap2 = []
for i in range(len(temp)):
    #첫번째것이 먼저들어간다
    heapq.heappush(heap2, (-temp[i], temp[i]))
heapq.heappush(heap2, (-1, 1))
print(heap2)
while heap2:
    print(heapq.heappop(heap2)[1], end=" ")
    print(heapq.heappop(heap2)[0] * -1, end=" ")


# 최대힙 두번째 방법
temp = [7,2,5,3,4,6]
heap2 = []
for i in range(len(temp)):
    #첫번째것이 먼저들어간다
    heapq.heappush(heap2, (-temp[i]))
heapq.heappush(heap2, (-1))
print(heap2)
while heap2:
    print(heapq.heappop(heap2)*-1, end=" ")

# 그래프알고리즘을 할때 쓰일수있다

