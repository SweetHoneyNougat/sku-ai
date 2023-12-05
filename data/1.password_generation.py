from random import randint

ENDL = '\n'
SYMBOLS = "`~!@#$%^&*()-_=+[{]}\\|;:'\",./?"

# 패턴 리스트를 생성하는 함수
def generate_patterns(wordlist, in_digit = True, in_symbol = True, in_upper = True, in_lower = True, in_word = True):
    patterns = set()

    if in_digit:
        for i in range(48, 58): # 0 ~ 9
            patterns.add(chr(i))
    if in_symbol:
        for i in SYMBOLS:
            patterns.add(i)
    if in_upper:
        for i in range(65, 91): # A ~ Z
            patterns.add(chr(i))
    if in_lower:
        for i in range(97, 123): # a ~ z
            patterns.add(chr(i))
    if in_word:
        for i in wordlist:
            patterns.add(i)

    return sorted(patterns, key = lambda x: len(x))

# 패턴들을 조합하여 원하는 길이의 비밀번호를 생성하는 함수
#
# [ 파라미터 ]
# length: 길이
# patterns: 패턴 리스트
def generate_password(length, patterns):
    password = []
    current_length = 0
    r = len(patterns)-1

    while current_length < length:
        while length-current_length < len(patterns[r]):
            r -= 1
        pattern = patterns[randint(0, r)] # [0, r] 범위 내의 패턴 선택
        password.append(pattern)
        current_length += len(pattern)

    return ''.join(password)

def readlines_without_endl(path):
    with open(path, 'r') as f:
        l = [i.strip() for i in f.readlines()]
    return l

# 비밀번호들을 생성하고, 파일에 기록하는 함수
#
# [ 파라미터 ]
# path: 비밀번호 파일의 저장 경로
# patterns: 패턴 리스트
# num_password: 생성할 비밀번호의 수
# length: 생성할 비밀번호의 길이
def write_password_data(path, patterns, num_password, length):
    passwords = set()

    for i in range(num_password):
        password = generate_password(length, patterns)
        while password in passwords: # 비밀번호 중복 방지
            password = generate_password(length, patterns)
        passwords.add(password)

    for i in sorted(passwords):
        with open(path, 'a') as f:
            f.write(i+ENDL)

# 단어 리스트 불러오기
wordlist = readlines_without_endl("data\\wordlist\\lower10000.txt")
wordlist.extend(readlines_without_endl("data\\wordlist\\upper10000.txt"))
wordlist.extend(readlines_without_endl("data\\wordlist\\capitalize10000.txt"))
wordlist.extend(readlines_without_endl("data\\wordlist\\custom.txt"))

def f(name, a, b, num, in_digit, in_symbol, in_upper, in_lower, in_word):
    patterns = generate_patterns(wordlist, in_digit, in_symbol, in_upper, in_lower, in_word)
    for i in range(a, b+1):
        write_password_data(f"data\\data_temp\\{name}\\{name}{i}.in", patterns, num, i)

if __name__ == '__main__':
    '''
    # s8 ~ s16
    f("s", 8, 16, 1000,
      in_digit = False,
      in_symbol = True,
      in_upper = False,
      in_lower = False,
      in_word = False)
    '''

    '''
    # u8 ~ u16
    f("u", 8, 16, 1000,
      in_digit = False,
      in_symbol = False,
      in_upper = True,
      in_lower = False,
      in_word = False)
    '''

    '''
    # w8 ~ w16
    f("w", 8, 16, 3000,
      in_digit = False,
      in_symbol = False,
      in_upper = False,
      in_lower = False,
      in_word = True)
    '''

    '''
    # nw8 ~ nw16
    f("nw", 8, 16, 1000,
      in_digit = True,
      in_symbol = False,
      in_upper = False,
      in_lower = False,
      in_word = True)
    '''

    '''
    # ulw8 ~ ulw16
    f("ulw", 8, 16, 1000,
      in_digit = False,
      in_symbol = False,
      in_upper = True,
      in_lower = True,
      in_word = True)
    '''

    '''
    # nul'8 ~ nul'16
    f("nul'", 8, 16, 1000,
      in_digit = True,
      in_symbol = False,
      in_upper = True,
      in_lower = True,
      in_word = False)
    '''
    
    '''
    # ul8 ~ ul16
    f("ul", 8, 16, 1000,
      in_digit = True,
      in_symbol = False,
      in_upper = True,
      in_lower = True,
      in_word = True)
    '''

    '''
    # wordlist/lower10000
    wordlist = readlines_without_endl("data\\wordlist\\lower10000.txt")
    f("wl", 8, 16, 3000,
      in_digit = False,
      in_symbol = False,
      in_upper = False,
      in_lower = False,
      in_word = True)
    '''

    '''
    # wordlist/upper10000
    wordlist = readlines_without_endl("data\\wordlist\\upper10000.txt")
    f("wu", 8, 16, 3000,
      in_digit = False,
      in_symbol = False,
      in_upper = False,
      in_lower = False,
      in_word = True)
    '''

    '''
    # wordlist/capitalize10000
    wordlist = readlines_without_endl("data\\wordlist\\capitalize10000.txt")
    f("wc", 8, 16, 3000,
      in_digit = False,
      in_symbol = False,
      in_upper = False,
      in_lower = False,
      in_word = True)
    '''

    #f("all", 8, 16, 10000, True, True, True, True, True)

    f("test", 8, 8, 1000, True, True, True, True, True)
