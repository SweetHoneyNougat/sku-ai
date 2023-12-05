import requests, time, os
from bs4 import BeautifulSoup

ENDL = '\n'

def crawling(url, data = {}, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36'}):
    response = requests.post(url, data = data, headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

# 비밀번호가 해킹당했는지 확인하는 함수
#
# [ 파라미터 ]
# password: 비밀번호
#
# [ 반환값 ]
# 1: 해킹 당함
# 0: 해킹 당하지 않음
# -1: 오류
def hacked(password):
    url = "https://haveibeenpwned.com/Passwords"
    data = { "Password": password }
    soup = crawling(url, data)

    result = soup.select('div.pwnedSearchResult.in')[0].h2.get_text(strip = True)
    if result == "Oh no — pwned!": return 1
    if result == "Good news — no pwnage found!": return 0
    return -1

def readlines_without_endl(path):
    with open(path, 'r') as f:
        l = [i.strip() for i in f.readlines()]
    return l

# 각 비밀번호마다 해킹당했는지 확인하여 레이블링을 하고, 파일에 기록하는 함수
#
# [ 파라미터 ]
# path: 레이블 파일의 저장 경로
# passwords: 비밀번호 파일 경로
# start_index: 비밀번호 파일의 시작 줄
# waiting_time: 웹 크롤링 시간 간격
def labeling(path, passwords, start_index, waiting_time):
    for i in range(start_index, len(passwords)):
        check = hacked(passwords[i])

        with open(path, 'a') as f:
            f.write(str(check)+ENDL)

        print(f"{i}: [{passwords[i]}, {check}]")
        time.sleep(waiting_time) # 너무 빨리 크롤링하지 말 것

if __name__ == '__main__':
    passwords_path = input("passwords path: ")
    passwords = readlines_without_endl(passwords_path)

    path = os.path.splitext(passwords_path)[0]+".out"
    if os.path.exists(path): # 이어서 하기
        start_index = len(readlines_without_endl(path))
        print(f"index {start_index}부터 시작")
        labeling(path, passwords, start_index, 1)
    else: # 처음부터 하기
        print(f"처음부터 시작")
        labeling(path, passwords, 0, 1)
