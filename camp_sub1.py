from pymongo import mongo_client
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

host = "localhost"
port = 27017
client = mongo_client.MongoClient(host, port)
db = client["Test"]
col = db["Testing"]  
# col.drop()

# a = list(range(1,8220))
# a.append(list(range(99997,101000)))
# # for x in range(99997,101000):
# for x in range(1,10):
#     a.append(x)
# 상세 페이지 크롤링
for x in range(1,10):
    if x == 2474:
        continue
    
    base_url = "https://www.gocamping.or.kr/bsite/camp/info/read.do?c_no="+str(x)+"&viewType=read01&listOrdrTrget=frst_register_pnttm"
    response = requests.get(base_url)
    source = response.text
    soup = BeautifulSoup(source, "lxml")
    # x = soup.select_one("#table_type03 > div > table > tbody > tr:nth-child(1)")
    # 2474 문제 있는 url이어서 pass
    # 캠프 이름
    camp_name = soup.find("p", class_="camp_name")
    # option 1
    detail1 = soup.select_one("#cont_inner > div.sub_layout.layout > article > header > div > div.cont_tb > table > tbody > tr:nth-child(1)")
    
    
    # option 2
    detail2 = soup.select_one("#cont_inner > div.sub_layout.layout > article > header > div > div.cont_tb > table > tbody > tr:nth-child(2)")
   
    # option 3
    detail3 = soup.select_one("#cont_inner > div.sub_layout.layout > article > header > div > div.cont_tb > table > tbody > tr:nth-child(3)")
   
    # option 4
    detail4 = soup.select_one("#cont_inner > div.sub_layout.layout > article > header > div > div.cont_tb > table > tbody > tr:nth-child(4)")
    
    # option 5
    detail5 = soup.select_one("#cont_inner > div.sub_layout.layout > article > header > div > div.cont_tb > table > tbody > tr:nth-child(5)")

    # option 6
    detail6 = soup.select_one("#cont_inner > div.sub_layout.layout > article > header > div > div.cont_tb > table > tbody > tr:nth-child(6)")
    
    # option 7
    detail7 = soup.select_one("#cont_inner > div.sub_layout.layout > article > header > div > div.cont_tb > table > tbody > tr:nth-child(7)")
    
    # option 8
    detail8 = soup.select_one("#cont_inner > div.sub_layout.layout > article > header > div > div.cont_tb > table > tbody > tr:nth-child(8)")
    
    # option 9
    detail9 = soup.select_one("#cont_inner > div.sub_layout.layout > article > header > div > div.cont_tb > table > tbody > tr:nth-child(9)")
    
    info = soup.select_one("#cont_inner > div.sub_layout.layout > article > header > div > div.cont_tb > table") # 1번째 문단
    ss = soup.find("tbody", class_="t_c") # 2번째 문단
    if info == None:
        print("페이지 없음", x)
        pass
    else:
        if detail3 == None:
            print( "번호:", x ,"캠프 이름: ", camp_name.text.strip())
            print("상세설명1", detail1.text.strip())
            print("상세설명2", detail2.text.strip())
            dict = {"_id":x,"캠프 이름":re.sub(r"\s", "", camp_name.text),"주소":re.sub(r"\s", "", detail1.text),"문의처":re.sub(r"\s", "", detail2.text)}
            col.insert_one(dict)
            
        elif detail4 == None:
            print( "번호:", x ,"캠프 이름: ", camp_name.text.strip())
            print("상세설명1", detail1.text.strip())
            print("상세설명2", detail2.text.strip())
            print("상세설명3", detail3.text.strip())
            dict = {"_id":x,"캠프 이름":re.sub(r"\s", "", camp_name.text),"주소":re.sub(r"\s", "", detail1.text),"문의처":re.sub(r"\s", "", detail2.text),"캠핑장 환경":re.sub(r"\s", "", detail3.text)}
            col.insert_one(dict)
         
        elif detail5 == None:
            print( "번호:", x ,"캠프 이름: ", camp_name.text.strip())
            print("상세설명1", detail1.text.strip())
            print("상세설명2", detail2.text.strip())
            print("상세설명3", detail3.text.strip())
            print("상세설명4", detail4.text.strip())
            dict = {"_id":x,"캠프 이름":re.sub(r"\s", "", camp_name.text),"주소":re.sub(r"\s", "", detail1.text),"문의처":re.sub(r"\s", "", detail2.text),"캠핑장 환경":re.sub(r"\s", "", detail3.text), "캠핑장 유형":re.sub(r"\s", "", detail4.text)}
            col.insert_one(dict)
       
        elif detail6 == None:
            print( "번호:", x ,"캠프 이름: ", camp_name.text.strip())
            print("상세설명1", detail1.text.strip())
            print("상세설명2", detail2.text.strip())
            print("상세설명3", detail3.text.strip())
            print("상세설명4", detail4.text.strip())
            print("상세설명5", detail5.text.strip())
            dict = {"_id":x,"캠프 이름":re.sub(r"\s", "", camp_name.text),"주소":re.sub(r"\s", "", detail1.text),"문의처":re.sub(r"\s", "", detail2.text),"캠핑장 환경":re.sub(r"\s", "", detail3.text), "캠핑장 유형":re.sub(r"\s", "", detail4.text), "운영기간":re.sub(r"\s", "", detail5.text)}
            col.insert_one(dict)
      
            
        elif detail7 == None:
            print( "번호:", x ,"캠프 이름: ", camp_name.text.strip())
            print("상세설명1", detail1.text.strip())
            print("상세설명2", detail2.text.strip())
            print("상세설명3", detail3.text.strip())
            print("상세설명4", detail4.text.strip())
            print("상세설명5", detail5.text.strip())
            print("상세설명6", detail6.text.strip())
            dict = {"_id":x,"캠프 이름":re.sub(r"\s", "", camp_name.text),"주소":re.sub(r"\s", "", detail1.text),"문의처":re.sub(r"\s", "", detail2.text),"캠핑장 환경":re.sub(r"\s", "", detail3.text), "캠핑장 유형":re.sub(r"\s", "", detail4.text), "운영기간":re.sub(r"\s", "", detail5.text), "운영일":re.sub(r"\s", "", detail6.text)}
            col.insert_one(dict)

            
        elif detail8 == None:
            print( "번호:", x ,"캠프 이름: ", camp_name.text.strip())
            print("상세설명1", detail1.text.strip())
            print("상세설명2", detail2.text.strip())
            print("상세설명3", detail3.text.strip())
            print("상세설명4", detail4.text.strip())
            print("상세설명5", detail5.text.strip())
            print("상세설명6", detail6.text.strip())
            print("상세설명7", detail7.text.strip())
            dict = {"_id":x,"캠프 이름":re.sub(r"\s", "", camp_name.text),"주소":re.sub(r"\s", "", detail1.text),"문의처":re.sub(r"\s", "", detail2.text),"캠핑장 환경":re.sub(r"\s", "", detail3.text), "캠핑장 유형":re.sub(r"\s", "", detail4.text), "운영기간":re.sub(r"\s", "", detail5.text), "운영일":re.sub(r"\s", "", detail6.text), "홈페이지":re.sub(r"\s", "", detail7.text)}
            col.insert_one(dict)
     
            
        elif detail9 == None:
            print( "번호:", x ,"캠프 이름: ", camp_name.text.strip())
            print("상세설명1", detail1.text.strip())
            print("상세설명2", detail2.text.strip())
            print("상세설명3", detail3.text.strip())
            print("상세설명4", detail4.text.strip())
            print("상세설명5", detail5.text.strip())
            print("상세설명6", detail6.text.strip())
            print("상세설명7", detail7.text.strip())
            print("상세설명8", detail8.text.strip())
            dict = {"_id":x,"캠프 이름":re.sub(r"\s", "", camp_name.text),"주소":re.sub(r"\s", "", detail1.text),"문의처":re.sub(r"\s", "", detail2.text),"캠핑장 환경":re.sub(r"\s", "", detail3.text), "캠핑장 유형":re.sub(r"\s", "", detail4.text), "운영기간":re.sub(r"\s", "", detail5.text), "운영일":re.sub(r"\s", "", detail6.text), "홈페이지":re.sub(r"\s", "", detail7.text), "예약방법":re.sub(r"\s", "", detail8.text)}
            col.insert_one(dict)
   
        else:
            print( "번호:", x ,"캠프 이름: ", camp_name.text.strip())
            print("상세설명1", detail1.text.strip())
            print("상세설명2", detail2.text.strip())
            print("상세설명3", detail3.text.strip())
            print("상세설명4", detail4.text.strip())
            print("상세설명5", detail5.text.strip())
            print("상세설명6", detail6.text.strip())
            print("상세설명7", detail7.text.strip())
            print("상세설명8", detail8.text.strip())
            print("상세설명9", detail9.text.strip())
            re.sub(r"\s", "", detail1.text)
            a = detail1.text.strip().split("\n",2)
            print(a[1])
            dict = {"_id":x,"캠프 이름":re.sub(r"\s", "", camp_name.text),"주소":detail1.text.split(),"문의처":re.sub(r"\s", "", detail2.text.split()),"캠핑장 환경":re.sub(r"\s", "", detail3.text.split()), "캠핑장 유형":re.sub(r"\s", "", detail4.text), "운영기간":re.sub(r"\s", "", detail5.text), "운영일":re.sub(r"\s", "", detail6.text), "홈페이지":re.sub(r"\s", "", detail7.text), "예약방법":re.sub(r"\s", "", detail8.text),"주변이용가능시설":re.sub(r"\s", "", detail9.text)}
            col.insert_one(dict)