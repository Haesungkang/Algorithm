import sys
sys.stdin = open("input2.txt", "r")

N = int(input())

order = list(map(int, input().split()))
result = []

for i in range(N):
    a = order[i]
    # insert를 이용해서 순서에 맞게 삽입한다
    result.insert(len(result)-a,(i+1))

for i in result:
    print(i, end=' ')



