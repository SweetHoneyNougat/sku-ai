# Original: data/5.feature_extraction.py

import os, sys

SYMBOLS = "`~!@#$%^&*()-_=+[{]}\\|;:'\",./?"

# 비밀번호의 각 문자마다 문자 범위 [left, right]에 있으면 카운트하는 함수
def count_in_range(password, left, right):
    cnt = 0

    for i in password:
        if left <= i <= right:
            cnt += 1

    return cnt

# 비밀번호의 각 문자마다 리스트 l 안의 문자에 해당하면 카운트하는 함수
# l: 매칭할 문자들이 들어있는 리스트
def count_in_list(password, l):
    cnt = 0

    for i in password:
        if i in l:
            cnt += 1

    return cnt

# 반복된 문자열의 최대 길이를 구하는 함수
def max_repeated_characters(password):
    mx = cnt = 1
    n = len(password)

    for i in range(n-1):
        if password[i] == password[i+1]: cnt += 1
        else: cnt = 1

        mx = max(mx, cnt)

    return mx

# a와 b가 같은 종류의 문자인지 판별하는 함수
def is_same_type(a, b):
    return (a.isnumeric() and b.isnumeric()) \
        or (a in SYMBOLS and b in SYMBOLS) \
        or (a.isupper() and b.isupper()) \
        or (a.islower() and b.islower())

# 연속된 문자열의 최대 길이를 구하는 함수
# d: 공차
def max_consecutive_characters(password, d):
    mx = cnt = 1
    n = len(password)

    for i in range(n-1):
        if is_same_type(password[i], password[i+1]) and ord(password[i+1])-ord(password[i]) == d: cnt += 1
        else: cnt = 1

        mx = max(mx, cnt)

    return mx

# 사전을 불러오는 함수
# dir_path: 사전 파일들이 있는 디렉터리 위치
def load_dict(dir_path):
    dict_ = []

    for i in os.listdir(dir_path):
        with open(dir_path+'/'+i, 'r', encoding='utf-8') as f:
            dict_.extend([i.strip() for i in f.readlines()])

    return dict_

# 비밀번호의 특징을 추출하는 함수
def extract_feature(p, dict_):
    return [count_in_range(p, '0', '9'),
            count_in_list(p, SYMBOLS),
            count_in_range(p, 'A', 'Z'),
            count_in_range(p, 'a', 'z'),
            max_repeated_characters(p),
            max(max_consecutive_characters(p, 1), max_consecutive_characters(p, -1)),
            int(p in dict_)]

if __name__ == '__main__':
    args = sys.argv
    dict_ = load_dict("dict")
    for i in extract_feature(args[1], dict_): # 추출된 특징 출력
        print(end = f"{i} ")
