import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# DataFrame으로 csv 파일 읽기
df = pd.read_csv('info.csv')

# 산점도 행렬 (scatterplot matrix) 시각화
sns.pairplot(df)
plt.show()
