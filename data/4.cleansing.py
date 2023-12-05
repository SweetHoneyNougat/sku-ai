import pandas as pd

df = pd.read_csv("data\\csv\\original.csv")

# 비밀번호의 길이가 8 ~ 16자가 아니면 데이터 제거
df = df[df['password'].str.len() >= 8]
df = df[df['password'].str.len() <= 16]

# 비밀번호 내의 문자가 '숫자, 특수문자, 영문 대소문자'가 아니면 데이터 제거
pattern = r'^[a-zA-Z0-9\`\~\!\@\#\$\%\^\&\*\(\)\-\_\=\+\[\{\]\}\\\|\;\:\'\"\,\.\/\?]+$'
df = df[df['password'].str.match(pattern)]

# 중복 데이터 제거
df = df.drop_duplicates(subset=['password'])

df.to_csv("data\\csv\\cleansing.csv", index=False)

print(df)
