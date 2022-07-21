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

for x in range(1, 30):
    
    base_url = "https://www.gocamping.or.kr/bsite/camp/info/read.do?c_no=100459&viewType=read01&listOrdrTrget=frst_register_pnttm"
    if base_url == None:
        print("페이지 없음")
    else:
        response = requests.get(base_url)
        source = response.text
        # print(source)
        soup = BeautifulSoup(source, "html.parser")
        # # info = soup.find("table", class_="table")
        info = soup.select_one("#cont_inner > div.sub_layout.layout > article > header > div > div.cont_tb > table")
        print(info)

        