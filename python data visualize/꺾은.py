import pandas as pd
import matplotlib.pyplot as plt

# DataFrame으로 csv 파일 읽기
df = pd.read_csv('info.csv')

# 간단한 요약 통계량 출력
print(df.describe())

# 클래스에 따른 평균 키 계산
class_height_avg = df.groupby('class')['height_cm'].mean()

# 꺾은선 그래프로 시각화
class_height_avg.plot(kind='line', marker='o')
plt.xlabel('Class')
plt.ylabel('Average Height')
plt.title('Average Height by Class')
plt.xticks(rotation = 0)
plt.show()