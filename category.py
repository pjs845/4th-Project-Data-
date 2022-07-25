from unicodedata import category
from pymongo import mongo_client
import matplotlib.pyplot as plt
import pandas as pd

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
    print(cate)
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

df = pd.DataFrame(
   dict(
      names=kind,
      marks=kind_num
   )
)

plt.figure(figsize=(16,9))
df_sorted = df.sort_values('marks')
plt.bar('names', 'marks', data=df_sorted)
plt.title("캠핑장 유형", fontsize=25)
plt.show()
