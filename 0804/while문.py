# import sys
# sys.stdin = open('input.txt', 'r')

# 1-73까지의 숫자중에 3으로 끝나는 숫자만 출력
i = 0
while True:
    if i > 73:
        break
    if i % 10 == 3:
        print(i, end= ' ')
    i+=1




