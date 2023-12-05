import joblib
import numpy as np
from tensorflow import keras
import feature_extraction as fe

# scaler 불러오기
scaler = joblib.load("model\\results\\scaler.pkl")

# 모델 불러오기
model = keras.models.load_model("model\\results\\model.h5")

# 예측을 원하는 입력 값
password = input()
X = np.array([fe.extract_feature(password, fe.load_dict("data\\dict"))])

# 데이터 정규화
X = scaler.transform(X)

print("정규화 데이터:", X)

# 모델 예측
prediction = model.predict(X)
print(prediction[0][0])
