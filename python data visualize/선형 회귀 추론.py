#pip install scikit-learn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 데이터 불러오기
df = pd.read_csv('info.csv')

# 독립 변수(X)와 종속 변수(y) 설정
X = df[['height_cm']]
y = df['weight_kg']

# 훈련 데이터와 테스트 데이터로 분할 (예: 80% 훈련, 20% 테스트)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 선형 회귀 모델 학습
reg = LinearRegression()
reg.fit(X_train, y_train)

# 테스트 데이터에 대한 예측
y_pred = reg.predict(X_test)

# 모델 성능 평가
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# 결과 시각화
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred, color='red', marker='o', linestyle='-', label='Predicted')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Linear Regression: Height vs Weight')
plt.legend()
plt.show()