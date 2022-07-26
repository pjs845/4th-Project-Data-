from unicodedata import category
from pymongo import mongo_client
import matplotlib.pyplot as plt
import pandas as pd
import re
import numpy as np

plt.rcParams['font.family'] ='Malgun Gothic' # 윈도우, 구글 콜랩
plt.rcParams['axes.unicode_minus'] =False # 한글 폰트 사용시 마이너스 폰트 깨짐 해결

#몽고DB
host = "192.168.0.66"
port = 27017
client = mongo_client.MongoClient(host, port)
db = client["Camp"]
col = db["CampInfo"]  

docs = col.find({ "기타 정보": { "$regex": "^반려" }})
cnt = int()
whether_num = list()
whether = ["반려동물 동반 가능", "반려동물 동반 불가능", "반려동물 동반 소형견만 가능"]
possible = impossible = little_animal = int()

for x in docs:
    # print(x["기타 정보"])
    cate = x["기타 정보"].split(",")    
    # ca = re.sub(r"\s", " ", cate[0][0:16])
    cate = cate[0][0:17]
    cate = re.sub(r"^\s+|\s+$", "", cate)
    # print(cate)
    if cate == "반려동물 동반 가능".strip():
        possible = possible + 1
        # print("1")
    elif cate == "반려동물 동반 불가능".strip():
        impossible = impossible + 1
        # print("2")
    elif cate == "반려동물 동반 소형견만 가능".strip():
        little_animal = little_animal + 1
        # print("3")

whether_num.append((possible))
whether_num.append((impossible))
whether_num.append((little_animal))

df = pd.DataFrame(
   dict(
      names=whether,
      marks=whether_num
   )
)

df_sorted = df.sort_values('marks')
colors = ['saddlebrown', 'burlywood','rosybrown']
wedgeprops={'width': 0.8, 'edgecolor': 'maroon', 'linewidth': 2.8}
textfont = dict(size=11)
plt.figure(figsize=(10,4), facecolor='#fcf1e1')
plt.title("[ WITH PETS | 반려동물 (동반/비동반) 캠핑장 수 ]",fontweight ='bold', loc='center',color='dimgrey',fontsize =16)
plt.pie(df_sorted['marks'],labels=df_sorted['names'], autopct='%.0f%%', startangle=360, counterclock=False,pctdistance=0.7, colors=colors , wedgeprops=wedgeprops, shadow=True,textprops = textfont)
plt.legend(['소형견가능','동반가능','동반불가'], ncol= 1, loc=(-0.05,0.05), fontsize=10, fancybox=True) 
plt.show()
