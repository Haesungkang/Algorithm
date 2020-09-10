import sys
sys.stdin = open("sample_input_3.txt", "r")
from heapq import heapify

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input()).split())

    heapify(arr)

    v = (N-1)
