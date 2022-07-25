import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def locationbar(col):   
    plt.rcParams['font.family'] ='Malgun Gothic' # 윈도우, 구글 콜랩
    plt.rcParams['axes.unicode_minus'] =False # 한글 폰트 사용시 마이너스 폰트 깨짐 해결
    docs = col.find()
    cnt = int()
    locationnum = list()
    location = ["서울시", "부산시", "대구시", "인천시", "광주시", "대전시", "울산시", "세종시",
                "경기도", "강원도", "충청북도", "충청남도", "전라북도", "전라남도", "경상북도",
                "경상남도", "제주도"]
    seoul = busan = daegu = incheon = gwangju = daejun = ulsan = sejong = int()
    gyeonggi = gangwon = chungbuk = chungnam = junrabuk = junranam = gyeongsangbuk = gyeongsangnam = jeju = int()
    for x in docs:
        #print(x["캠핑장이름"])
        loc = x["캠핑장이름"].split()
        loc = loc[0][1:]
        #print(loc)
        if loc == "서울시":
            seoul = seoul + 1
        elif loc == "부산시":
            busan = busan + 1
        elif loc == "대구시":
            daegu = daegu + 1
        elif loc == "인천시":
            incheon = incheon + 1
        elif loc == "광주시":
            gwangju = gwangju + 1
        elif loc == "대전시":
            daejun = daejun + 1
        elif loc == "울산시":
            ulsan = ulsan + 1
        elif loc == "세종시":
            sejong = sejong + 1
        elif loc == "경기도":
            gyeonggi = gyeonggi + 1
        elif loc == "강원도":
            gangwon = gangwon + 1
        elif loc == "충청북도":
            chungbuk = chungbuk + 1
        elif loc == "충청남도":
            chungnam = chungnam + 1
        elif loc == "전라북도":
            junrabuk = junrabuk + 1
        elif loc == "전라남도":
            junranam = junranam + 1
        elif loc == "경상북도":
            gyeongsangbuk = gyeongsangbuk + 1
        elif loc == "경상남도":
            gyeongsangnam = gyeongsangnam + 1
        elif loc == "제주도":
            jeju = jeju + 1
    locationnum.append(seoul)
    locationnum.append(busan)
    locationnum.append(daegu)
    locationnum.append(incheon)
    locationnum.append(gwangju)
    locationnum.append(daejun)
    locationnum.append(ulsan)
    locationnum.append(sejong)
    locationnum.append(gyeonggi)
    locationnum.append(gangwon)
    locationnum.append(chungbuk)
    locationnum.append(chungnam)
    locationnum.append(junrabuk)
    locationnum.append(junranam)
    locationnum.append(gyeongsangbuk)
    locationnum.append(gyeongsangnam)
    locationnum.append(jeju)
    df = pd.DataFrame(
    dict(
        names=location,
        marks=locationnum
    )
    )
    plt.figure(figsize=(14,4), facecolor= 'w')
    df_sorted = df.sort_values('marks')
    plt.rc('axes', facecolor = 'linen', edgecolor = 'darkgrey', linewidth = 0.5)
    plt.rc('ytick', color = 'dimgrey')
    w = 0.5
    bary = np.arange(len(location))
    print(bary)
    plt.bar('names','marks', w, data=df_sorted,color='peru',align='edge', edgecolor='chocolate')
    plt.grid(color = 'w')
    plt.xticks(bary+w/2, df_sorted['names'], color ='dimgrey')
    plt.ylim(0,800) 
    plt.title("[ CAMPGROUND | 지역별 캠핑장 수 ]",loc='right',color='dimgrey',fontsize =13)
    plt.show()





