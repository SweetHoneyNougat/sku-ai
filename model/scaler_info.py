import joblib

# scaler 불러오기
scaler = joblib.load("model\\results\\scaler.pkl")

print(f"Mean: {scaler.mean_}")
print(f"Scale: {scaler.scale_}")
