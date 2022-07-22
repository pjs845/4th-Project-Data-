from pymongo import mongo_client
from bs4 import BeautifulSoup
import requests
import pandas as pd

#페이지 크롤링
url = "https://www.gocamping.or.kr/bsite/camp/info/read.do?c_no=28&viewType=read01&listOrdrTrget=frst_register_pnttm"
response = requests.get(url)
source = response.text

soup = BeautifulSoup(source, "html.parser")

info = soup.find("table", class_="table")
# print(info.text)

ss = soup.find("tbody", class_="t_c")
# print(ss.text)

import pandas as pd

df = pd.DataFrame()
li = {'문의처': None, '캠핑장 환경': None, '캠핑장 유형':None, '운영기간': None,
      '운영일':None, '홈페이지':None,'예약방법':None, '주변이용가능시설':None}
for x in range(1, 2):
    
    base_url = "https://www.gocamping.or.kr/bsite/camp/info/read.do?c_no=100459&viewType=read01&listOrdrTrget=frst_register_pnttm"
    if base_url == None:
        print("페이지 없음")
    else:
        response = requests.get(base_url)
        source = response.text
        # print(source)
        soup = BeautifulSoup(source, "html.parser")
        # # info = soup.find("table", class_="table")
        info = soup.select_one("#cont_inner > div.sub_layout.layout > article > header > div > div.cont_tb > table > tbody")
        html = pd.read_html(source, header=0)[0]
        df = pd.concat([df, html])
        print(df)
        dfname = df.columns
        df = df.set_index('주소').T.to_dict('list')
        print(df)
        li.update(df)
        print(dfname)
        print(li)
        print(type(df))
