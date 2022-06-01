import sys
sys.stdin = open('input.txt', 'r')

def findMatch(idx): #idx 패턴매칭 시작 인덱스
    global num
    for j in range(10):
        isMatch = True # Matching이 됐는지 안됐는지 확인하는 결과값
        for k in range(6):
            if bit[idx + k] != pwd[j][k]: # 패턴이 다른경우
                isMatch = False
                break
        if isMatch:
            num = j
            return True
    return False

pwd = ['001101','010011','111011','110001', '100011','110111','001011','111101','011001','101111']

s = input()
n = len(s)
# print(s)
bit =""  #2진수 표현을 저장

# print(ord('F'))   #ord : 문자의 아스키 코드를 리턴
for i in range(n):
    #16진수 -> 10진수
    d = ord(s[i])- ord('0') if '0' <= s[i] <= '9' else ord(s[i]) - ord('A') + 10
    # print(d)
    #10진수 -> 2진수 -> output
    for j in range(3,-1,-1):
        bit += '1' if d &(1 <<j) else '0'
#print(bit)

# 패턴매칭
idx = 0
num = 0   #패턴에 해당하는 번호
cnt = []

# for 구문말고 while구문도 생각해보면 좋을거같다
while idx < len(bit) - 6: #타겟 - 패턴길이의 만큼만 반복해서 확인
    if findMatch(idx):  #패턴매칭함수생성
        cnt.append(num)
        idx += 6
        pass
    else:
        idx += 1
#print(cnt)
print(",".join(map(str, cnt)))





# #2진수 -> (7bit씩 끊어서) 10진수
# n2 = len(output)//7 #7개씩 묶으면 몇개가 되는지?
# remain = len(output)%7 -1   #7개씩 묶고 남은 개수
# for i in range(n2):
#     digit = 0   #10진수저장
#     for j in range(6,-1,-1):
#         digit += int(output[i*7 + j]) * (2**(6-j))
#     print(digit)
# digit = 0
# for j in range(remain,-1,-1):
#     digit += int(output[n2*7 + j]) * (2**(remain-j))
# print(digit)






#0DEC

# 16진수 문자로 이루어진 1차 배열이 주어질 때 암호비트패턴을 찾아 차례대로 출력하시오. 암호는 연속되어있다.

# 0DEC
# 3564
# 00 001101 111011 00







