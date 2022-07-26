from unicodedata import category
from pymongo import mongo_client
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.family'] ='Malgun Gothic' # 윈도우, 구글 콜랩
plt.rcParams['axes.unicode_minus'] =False # 한글 폰트 사용시 마이너스 폰트 깨짐 해결

#몽고DB
host = "192.168.0.66"
port = 27017
client = mongo_client.MongoClient(host, port)
db = client["Camp"]
col = db["CampInfo"]  


docs = col.find()
cnt = int()
kind_num = list()
kind = ["일반야영장", "자동차야영장", "글램핑", "카라반"]
nomal = car = gram = caravan = int()

for x in docs:
    #print(x["캠핑장 유형"])
    cate = x["캠핑장 유형"].split(",")
    #cate = cate[0][0:]
    #print(cate)
    for y in cate:
        if y == "일반야영장":
            nomal = nomal + 1
        elif y == "자동차야영장":
            car = car + 1
        elif y == "글램핑":
            gram = gram + 1
        elif y == "카라반":
            caravan = caravan + 1
            
kind_num.append(nomal)
kind_num.append(car)
kind_num.append(gram)
kind_num.append(caravan)

ratio = np.array(kind_num)
labels = np.array(kind)
explode = [0.05, 0, 0.07, 0]
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 3}
colors = ['#5bc0c9','#77d1ac','#cfacfa','#f7d797']
textpromps = dict(size=13, fontweight='bold', color='#42403e')
title_font = {
    'fontsize': 17,
    'fontweight': 'bold'
}
plt.title('<<Camping Category>>', fontdict=title_font, loc = 'left', pad=20)
plt.pie(kind_num, labels=kind, explode=explode, colors=colors, counterclock=False, startangle=90, wedgeprops=wedgeprops, autopct = '%.1f%%', pctdistance = 0.7, textprops = textpromps)
plt.legend(loc='upper right', fontsize=10)
plt.show()





