import pandas as pd
import matplotlib.pyplot as plt

# DataFrame으로 csv 파일 읽기
df = pd.read_csv('info.csv')

# 간단한 요약 통계량 출력
print(df.describe())

# 성별에 따른 평균 키 계산
gender_height_avg = df.groupby('gender')['height_cm'].mean()

# 막대 그래프로 시각화
gender_height_avg.plot(kind='bar', color=['b', 'r'])
plt.xlabel('Gender')
plt.ylabel('Average Height')
plt.title('Average Height by Gender')
plt.xticks(rotation = 0)
plt.show()
