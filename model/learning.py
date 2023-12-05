import pandas as pd
from tensorflow import keras
from sklearn.preprocessing import StandardScaler
import joblib
from sklearn.model_selection import train_test_split

df = pd.read_csv("data\\csv\\features.csv")
num_X = df.shape[1]-2 # 독립변수의 수

# 파라미터 설정
epochs = 25
batch_size = 32
verbose = 1
activation = 'sigmoid'
optimizer = 'rmsprop' # rmsprop, sgd, adam?
loss = 'binary_crossentropy'

# 독립변수 X, 종속변수 Y 선언
X = df.iloc[:, 2:].values # (length, ..., in_dict)
Y = df.iloc[:, 1].values # (label)

# 데이터 정규화
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 데이터를 학습, 검증, 테스트 데이터로 분할
# 학습 데이터: 70%
# 검증 데이터: 15%
# 테스트 데이터: 15%
X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.3, random_state=42)
X_val, X_test, Y_val, Y_test = train_test_split(X_temp, Y_temp, test_size=0.5, random_state=42)

# 로지스틱 회귀 모델 정의
model = keras.Sequential([
    keras.layers.Input(shape=(num_X,)),  # 입력 레이어
    keras.layers.Dense(1, activation=activation)  # 출력 레이어
])

# 모델 컴파일
model.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])

# 모델 학습
model.fit(X_train, Y_train, epochs=epochs, batch_size=batch_size, verbose=verbose, validation_data=(X_val, Y_val))

# 모델 평가
test_loss, test_acc = model.evaluate(X_test, Y_test)
print(f'\n테스트 정확도: {test_acc}')

# scaler 저장
joblib.dump(scaler, "model\\results\\scaler.pkl")

# 모델 저장
model.save("model\\results\\model.h5")
