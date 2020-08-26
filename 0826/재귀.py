'''
재귀 함수 : 자기자신을 호출하는 함수
'''

# def func(): #함수를 정의
#     print("hello")
#     func()
#
#
# func()

# 위에 코드를 그대로 실행하면 무한 반복 발생

'''
무한 반복에 빠지지 않게 하려면 어떻게 해야할까?
매개변수를 하나 받음
재귀 호출이 발생할떄마다 매개변수의 값이 변하도록 설정
재귀 함수에서 매개변수의 값을 이용해서 조건을 설정하고 일정조건으로 만족하면
리턴하도록 설정     
'''

# 나의풀이
# def func(n): #함수를 정의
#     if n == 1:
#         return print("hello")
#     print("hello")  # 조건식: 변수 < 0
#     func(n-1)
#
# func(5) # hello를 5번만 출력할수있도록 설정해보기

# 교수님풀이
# def func(k): #함수를 정의
#     if k <= 0:   # 조건식: 변수 < 0
#         return
#     print("hello")
#     func(k-1)
#
# func(5)

'''
재귀함수의 구조
- 기본파트
    : 적어도 하나의 재귀에 빠지지 않는 경우가 존재해야함.
- 유도파트 
    : 재귀를 반복하다보면 결국 기본파트에 수렴해야함.

'''

# 1~10까지의 합을 구하는 재귀함수를 만들어보세요.

# def sum(k, total):
#     if k <= 0:
#         print(total)
#         return
#     # print(k)
#     sum(k-1, total+k)
#
# sum(10, 0) #10을 줌

def sum2(k):
    if k == 0:
        return 0
    # print(k)
    return k + sum2(k-1)

print(sum2(10))
