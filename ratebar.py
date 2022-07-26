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
lo = 0
rate = 0
review = 0
ratelist = list()
reviewlist= list()
plt.rcParams['font.family'] ='Malgun Gothic' # 윈도우, 구글 콜랩
plt.rcParams['axes.unicode_minus'] =False # 한글 폰트 사용시 마이너스 폰트 깨짐 해결
for x in location:
    where = {"장소":{"$regex":"^"+x}}
    docs = col.find(where)
    for y in docs:
        try:
            if y["평점"] > 0:
                lo += 1
                rate = rate + y["평점"]
            else:
                pass
            review = review + y["리뷰수"]
        except TypeError:
            pass
    ratelist.append(round(rate/lo, 2))
    reviewlist.append(review)
    #print(lo)    
    lo = 0
    rate = 0
    review = 0
#print(ratelist) # 서울~제주 평균 평점
#print(reviewlist) #서울~제주 리뷰수
#print(location) # 서울~제주

ratedic = dict()
reviewdic = dict()
i = 0
for x in location:
    ratedic.update({x:ratelist[i]})
    reviewdic.update({x:reviewlist[i]})
    i += 1
#print(ratedic)
#print(reviewdic)

sorted_rate = sorted(ratedic.items(), reverse=False, key=lambda item: item[1])
sorted_rate = dict(sorted_rate)
sorted_review = sorted(reviewdic.items(), reverse=False, key=lambda item: item[1])
sorted_review = dict(sorted_review)



fig, ax = plt.subplots(figsize=(12,6))
plt.subplot(1,2,1)
plt.barh(range(len(sorted_rate)), list(sorted_rate.values()) , color='dodgerblue', alpha=0.7, edgecolor='black')
plt.yticks(range(len(sorted_rate)), list(sorted_rate.keys()))
plt.xlabel("평균 평점")

plt.subplot(1,2,2)
plt.barh(range(len(sorted_review)), list(sorted_review.values()), color='dodgerblue', alpha=0.7, edgecolor='black')
plt.yticks(range(len(sorted_review)), list(sorted_review.keys()))
plt.xlabel("총 리뷰수")

plt.show()

