import sys
sys.stdin = open('input_1.txt', 'r')

#회사에서 집가는 코스로


for tc in range(1, int(input())+1):
    c = int(input())
    arr = list(map(int, input().split()))
    company = arr[:2]
    home = arr[2:4]
    customer = arr[4:]

