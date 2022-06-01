'''
1~10까지의 합을 구하는 함수를 재귀함수로 구현
값을 리턴하는 형식
'''

#print(sum()) #여기에 결과값이 리턴

def sum10(v, s):

    if v == 11:
        print(s)
    else:
        sum10(v+1, s+v)

sum10(1, 0)


def sum(k):
    if k == 1:
        return 1
    return 1 + sum(k-1)