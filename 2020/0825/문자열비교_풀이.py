'''
비교 시작점
    0 ~ 긴문자열의 길이 - 짧은 문자열의 길이

문자열을 비교해서 같을 동안만 반복
    0단계
        0-0
        1-1
        2-2
    1단계
        0-1 ( 1 + 0 )
        1-2 ( 1 + 1 )
        2-3 ( 1 + 2 )
    2단계
        0-2 (2+0)
        1-3 (2+1)
        2-4 (2+2)
'''

import sys
sys.stdin = open('sample_input.txt', 'r')

def find():
    #시작점에서 설정 반복문
    for i in range(0, len(str2)-len(str1)+1):
        j = 0
        #0,1,2 늘어가면서 문자가 같을 동안만 비교하기
        while str1[j] == str2[i+j]: # 비교하고 있는 문자가 서로 같을 동안마나 반복
            j += 1
            if j == len(str1):
                return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    str1 = input() # 한줄읽기 -> 문자열을 저장
    str2 = input()
    r = find()
    print("#{} {}".format(tc, r))