from itertools import permutations
import sys

# T = int(input()) 정수 인풋 받아내기
# N, M = map(int, input().split())
# arrarylist = list(map(int, input().split())

numlist = [1,2,3,4,1,2,3,4]

hello = set(numlist)
world = list(numlist)

print(hello)
print(world)

numlist2 = [1,2,3,4]

world2 = list(permutations(numlist2,2))
world2length = len(world2)
print(world2)
print(world2length)