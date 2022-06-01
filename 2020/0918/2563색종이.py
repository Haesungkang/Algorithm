import sys
sys.stdin = open("input4.txt", "r")

t = int(input())
blank = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(t):
    i, j = map(int,input().split())
    for a in range(10):
        for b in range(10):
            blank[i-1+a][j-1+b] += 1

area = 0
for i in range(100):
    for j in range(100):
        if blank[i][j] != 0:
            area += 1

print(area)
