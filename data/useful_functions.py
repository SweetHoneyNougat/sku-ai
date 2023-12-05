import os

# 중복 데이터를 제거하는 함수
def compress(path):
    s = set()
    with open(path, 'r', encoding='utf-8') as f:
        s.update(f.readlines())
    with open(path, 'w', encoding='utf-8') as f:
        for i in sorted(s):
            f.write(i)

# label로 레이블링하는 함수
def labeling(path, label):
    n = 0
    with open(path, 'r', encoding='utf-8') as f:
        n = len(f.readlines())
    path = os.path.splitext(path)[0]+".out"
    with open(path, 'w', encoding='utf-8') as f:
        for i in range(n):
            f.write(f"{label}\n")

path = ""
for i in os.listdir(path):
    labeling(path+"\\"+i, 1)
#compress(input())
