s = "Reverse this string"
s_rev = ''
for ch in s:
    s_rev = ch + s_rev
print(s_rev)

# 방법2
# reverse : 리스트의 함수
s = "Reverse this string"
s_list = list(s)
s_list.reverse()
# print(s_list)
print("".join(s_list))

# 방법3
s = "Reverse this string" #문자열
print("".join(reversed(s)))

# 방법 4 : 슬라이싱 사용
s = "Reverse this string" #문자열
print(s[:])   #모든 영역 추출
print(s[0:3]) #0,1,2 (3은 포함안함)
print(s[3:0:-1]) #3,2,1
print(s[::-1])