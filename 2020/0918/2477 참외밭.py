import sys
sys.stdin = open("input5.txt", "r")

T = int(input())
length = []
for _ in range(6):
    i, j = map(int, input().split())
    length.append([i,j])

maxl = 0
maxh = 0
for i in range(6):
    if length[i][0] == 1 or length[i][0] == 2:
        if length[i][1] > maxl:
            maxl = length[i][1]
    if length[i][0] == 3 or length[i][0] == 4:
        if length[i][1] > maxh:
            maxh = length[i][1]
# print(length)
# print(maxl, maxh)
for i in range(6):
    if length[i][1] == maxl:
        final1 = length[(i+3)%6][1]
    if length[i][1] == maxh:
        final2 = length[(i+3)%6][1]

print((maxl*maxh - final1*final2)*T)
