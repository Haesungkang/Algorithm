'''
The Curious Case of Benjamin Button
'''
#input.split() 안쓰고
Str = input()
cnt = 0
words = False

for ch in Str:
    if ch == ' ': # 공백문자만나면 단어수 늘림
        if words: # 단어를 만났다면
            cnt +=1
            words = False
    else:
        words = True
if words:
    cnt += 1
print(cnt)

