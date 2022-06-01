'''
Mississipi
'''
Str = input()

count = [0 for _ in range(26)]

# print(ord("A"))
# print(ord("Z"))
# print(ord("a"))
for ch in Str:
    if ord(ch) <= 90: # 대문자
        # ord(ch) - ord("A")
        n = ord(ch) - ord("A")
    elif ord(ch) >= 97: # 소문자
        # print(ord(ch) - ord("a"))
        n = (ord(ch) - ord("a"))
    count[n] += 1
# print(count)
max = 0
maxidx = 0

for i in range(len(count)): # 최대값 찾기
    if max < count[i]:
        max = count[i]
        maxidx = i
cnt_max = 0
# print(max)
for c in count:
    if c == max:
        cnt_max += 1

ans = ""
if cnt_max > 1:
    ans = "?"
else:
    ans = chr(maxidx + 65)
print(ans)




