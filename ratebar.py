import matplotlib.pyplot as plt
from pymongo import mongo_client

#몽고DB
host = "localhost"
port = 27017
client = mongo_client.MongoClient(host, port)
db = client["soobindb"]
col = db["rate"]  

location = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종",
                "경기", "강원", "충북", "충남", "전북", "전남", "경북",
                "경남", "제주"]

def ratebar(col):
    plt.rcParams['font.family'] ='Malgun Gothic' # 윈도우, 구글 콜랩
    plt.rcParams['axes.unicode_minus'] =False # 한글 폰트 사용시 마이너스 폰트 깨짐 해결
    lo = 0
    result = 0
    ratelist = list()
    for x in location:
        where = {"장소":{"$regex":"^"+x}}
        docs = col.find(where)
        for y in docs:
            try:
                if y["평점"] > 0:
                    lo += 1
                    result = result + y["평점"]
                else:
                    pass
            except TypeError:
                pass
        ratelist.append(round(result/lo, 2))
        print(lo)    
        lo = 0
        result = 0
    print(ratelist) # 서울~제주 평균 평점
    print(location) # 서울~제주
ratebar(col)