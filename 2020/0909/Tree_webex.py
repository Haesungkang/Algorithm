def is_empty():
    return lastidx == 0

def is_full(): #트리가 가득찼는지 확인
    return lastidx == size

def add(n): #원소추가
    global lastidx
    if is_full():
        print("트리가 포화상태임")
        return
    lastidx += 1
    tree[lastidx] = n

def preorder(idx):  #부모, 왼, 오른쪽 -> VLR
    if idx <= lastidx:
    #현재노드 방문 (출력)
        print(tree[idx], end=" ")
    #왼쪽
    preorder(2*idx)      #왼쪽자식
    #오른쪽
    preorder(2*idx+1)      #오른쪽자식

# 중위순회
def inorder(idx):
    pass

# 후위순회
def postorder():
    pass


size = 15   # 배열크기 지정
tree = [0] * (size+1)
lastidx = 1     #마지막에 들어온 원소가 위치할 인덱스

#원소 넣기 : A,B,C,D...
for i in range(0, 10):
    #원소 넣기
    # print(chr(i+65)
    add(chr(i+65))

print(tree)


