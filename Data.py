import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic' # 윈도우, 구글 콜랩
plt.rcParams['axes.unicode_minus'] =False # 한글 폰트 사용시 마이너스 폰트 깨짐 해결

df = pd.read_csv("C:/PJS/project/4차 Data/4th-Project-Data-/지속적으로_참여하는_여가활동_분야_및_활동_관광_활동_20220721172818.csv", encoding='cp949')
df.fillna(0, inplace=True)
print(df.columns)