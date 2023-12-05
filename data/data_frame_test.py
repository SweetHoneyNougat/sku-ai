import pandas as pd

df = pd.read_csv("data\\csv\\cleansing.csv")

def df_label(n):
    return df[df['label'] == n]

print(df[df['password'] == "`/^]),.?^%)"])
