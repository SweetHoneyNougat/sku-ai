import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import feature_extraction as fe

# scaler 불러오기
scaler = joblib.load("model\\results\\scaler.pkl")

# 모델 불러오기
model = keras.models.load_model("model\\results\\model.h5")

df = pd.read_csv("data\\csv\\features.csv")

# 독립변수 X, 종속변수 Y 선언
X = df.iloc[:, 2:].values # (length, ..., in_dict)
Y = df.iloc[:, 1].values # (label)

# 데이터 정규화
X = scaler.transform(X)

# 데이터를 학습, 검증, 테스트 데이터로 분할
# 학습 데이터: 70%
# 검증 데이터: 15%
# 테스트 데이터: 15%
X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.3, random_state=42)
X_val, X_test, Y_val, Y_test = train_test_split(X_temp, Y_temp, test_size=0.5, random_state=42)

# 모델 평가
test_loss, test_acc = model.evaluate(X_test, Y_test)
print(f'\n테스트 정확도: {test_acc}')

Y_pred = (model.predict(X_test) >= 0.5).astype(int)
#print(Y_pred)
mat = confusion_matrix(Y_test, Y_pred)
print(f"혼동 행렬:\n{mat}")

'''
plt.scatter(Y_pred, Y_test, color='blue', marker='o')
plt.xlabel('predicted value')
plt.ylabel('actual value')
plt.legend()
plt.show()
'''
