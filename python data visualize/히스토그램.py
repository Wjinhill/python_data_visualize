import pandas as pd
import matplotlib.pyplot as plt

# DataFrame으로 csv 파일 읽기
df = pd.read_csv('info.csv')

# height_cm의 히스토그램 시각화
plt.hist(df['height_cm'], bins=20, color='blue', alpha=0.7)
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.title('Distribution of Height')
plt.show()

# weight_kg의 히스토그램 시각화
plt.hist(df['weight_kg'], bins=20, color='red', alpha=0.7)
plt.xlabel('Weight')
plt.ylabel('Frequency')
plt.title('Distribution of Weight')
plt.show()