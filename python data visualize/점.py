
#pip install matplotlib pandas 하고 시작한다 가정

import pandas as pd
import matplotlib.pyplot as plt

# DataFrame으로 csv 파일 읽기
df = pd.read_csv('info.csv')

# 간단한 요약 통계량 출력
print(df.describe())

# 키와 몸무게의 관계 시각화하기
plt.scatter(df['height_cm'], df['weight_kg'])
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Height vs Weight')
plt.show()

