import sys

sys.stdin = open('./inputfolder/input3.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print(arr)