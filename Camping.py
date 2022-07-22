from pymongo import mongo_client
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pymongo
import webbrowser
import folium
from bs4 import BeautifulSoup
import requests
import time
from urllib.request import urlopen
from urllib import parse
from urllib.request import Request
from urllib.error import HTTPError
import json
import numpy as np

id = 1
#몽고DB
host = "localhost"
port = 27017
client = mongo_client.MongoClient(host, port)
db = client["soobindb"]
col = db["site"]  
#col.drop()
#페이지 크롤링
url = "https://www.gocamping.or.kr/bsite/camp/info/list.do?pageUnit=10&searchKrwd=&listOrdrTrget=last_updusr_pnttm&pageIndex=1"
response = requests.get(url)
source = response.text
# print(source)

soup = BeautifulSoup(source, "html.parser")
# 1. 필요한 정보 가져오는 테스트 
# # camp_info = soup.find("div", id="cont_inner")
# print(camp_info)


# 2. 마지막 페이지 가져오기 
# 2-1. 마지막 페이지를 가져오려다 보니 id, class가 없어 find() 함수가 아닌 select_one 함수를 이용해 함
li = soup.select_one("#cont_inner > div > div.paging > ul > li:nth-child(14) > a")
x = li["href"]
y = x.split("=")
print(y)
last_page = y[-1]
print(last_page)

# 각 페이지 읽어오기 ( 마지막 311페이지까지 )
import pandas as pd
df = pd.DataFrame()
base_url = "https://www.gocamping.or.kr/bsite/camp/info/list.do?pageUnit=10&searchKrwd=&listOrdrTrget=last_updusr_pnttm"
#for page in range(1, int(last_page)+1): # 311페이지가 마지막이라 +1
for page in range(1, 2): #너무 많아서 2페이지만 테스트 하기용
    url = "{}&pageIndex={}".format(base_url, page) # page 부분이 1~ 311까지 반복
    response = requests.get(url, headers={"User-agent":"Mozilla/5.0"})
    source = response.text
    soup = BeautifulSoup(source, "html.parser")
    camps_info = soup.find("div", class_="camp_search_list") # 한 페이지에 캠핑정보 전체 긁어오기
    camp_info = soup.find("div", class_ ="camp_cont") # 한 문단의 정보씩 //근데 첫문단 밖에 안됨
    for x in range(1,11):
        comp_bar1 = soup.select_one("#cont_inner > div > div.camp_search_list > ul > li:nth-child("+str(x)+") > div > div > p > span.item_t01")
        comp_bar2 = soup.select_one("#cont_inner > div > div.camp_search_list > ul > li:nth-child("+str(x)+") > div > div > p > span.item_t02")
        comp_bar3 = soup.select_one("#cont_inner > div > div.camp_search_list > ul > li:nth-child("+str(x)+") > div > div > p > span.item_t03")
        comp_bar4 = soup.select_one("#cont_inner > div > div.camp_search_list > ul > li:nth-child("+str(x)+") > div > div > p > span.item_t04")
        comp_loc = soup.select_one("#cont_inner > div > div.camp_search_list > ul > li:nth-child("+str(x)+") > div > div > h2 > a")
        comp_exp = soup.select_one("#cont_inner > div > div.camp_search_list > ul > li:nth-child("+str(x)+") > div > div > span.camp_txt > a")
        comp_loc2 = soup.select_one("#cont_inner > div > div.camp_search_list > ul > li:nth-child("+str(x)+") > div > div > ul > li.addr")
        comp_num = soup.select_one("#cont_inner > div > div.camp_search_list > ul > li:nth-child("+str(x)+") > div > div > ul > li.call_num")
        comp_Facilities = soup.select_one("#cont_inner > div > div.camp_search_list > ul > li:nth-child("+str(x)+") > div > div > div")
        comp_image = soup.select_one("#cont_inner > div > div.camp_search_list > ul > li:nth-child("+str(x)+") > div > a > div > img")
        img = """<img src="https://www.gocamping.or.kr"""+comp_image['src']+"""" height="180" width="280">"""
        
        if comp_num == None:  
            dict = {"_id":id,"사업체":comp_bar1.text,"리뷰수":comp_bar2.text,"조회수":comp_bar3.text,"추천수":comp_bar4.text,"캠핑장이름":comp_loc.text,"캠핑장설명":comp_exp.text,"지역이름":comp_loc2.text,"전화번호":"None","캠핑장정보":"None", "이미지":img}
            col.insert_one(dict)
            
        else:
            #print(comp_num.text)
            dict = {"_id":id,"사업체":comp_bar1.text,"리뷰수":comp_bar2.text,"조회수":comp_bar3.text,"추천수":comp_bar4.text,"캠핑장이름":comp_loc.text,"캠핑장설명":comp_exp.text,"지역이름":comp_loc2.text,"전화번호":comp_num.text,"캠핑장정보":"None", "이미지":img}
            col.insert_one(dict)
            
            
        if comp_Facilities == None:
            pass
        else:
            where = {"_id":id} 
            new = {"$set": {"캠핑장정보":comp_Facilities.text}}
            col.update_one(where, new)
            
        id+=1
    
    # html = pd.read_csv(camps_info.text)
    # camps_info.text.split("\\n")
    # print(html)
    # print(camp_info.text)
    
question = input("캠핑장이름을 입력하세요(주소를 입력하고 싶으면 '주소'입력): ")
if question == '주소':
    question = input("주소를 입력해주세요: ")
    where = {"지역이름":{"$regex":question}}
else:
    where = {"캠핑장이름":{"$regex":question}}

docs = col.find(where)

#naver map api key
client_id = 'k3y82rodr8';    # 본인이 할당받은 ID 입력
client_pw = '6STyg87wDH81UANRy4ameDXDRE0Vxie1w09HfYdU';    # 본인이 할당받은 Secret 입력

api_url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='


# 네이버 지도 API 이용해서 위경도 찾기
location = list()
name = list()
info = list()
imglist = list()    
for x in docs:
    add = x["지역이름"]
    add_urlenc = parse.quote(add)  #한글 인코딩
    url = api_url + add_urlenc
    request = Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id) #아이디 요청
    request.add_header('X-NCP-APIGW-API-KEY', client_pw) #비밀번호 요청
    try:
        response = urlopen(request)
    except HTTPError as e:
        print('HTTP Error!')
        latitude = None
        longitude = None
    else:
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read().decode('utf-8')
            response_body = json.loads(response_body)   # json
            if response_body['addresses'] == [] :
                print("'result' not exist!")
                latitude = None
                longitude = None
            else:
                latitude = response_body['addresses'][0]['y']
                longitude = response_body['addresses'][0]['x']
                print("Success!")
                location.append([latitude, longitude])
                name.append(x["캠핑장이름"])
                info.append([x["지역이름"], x["전화번호"]])
                imglist.append(x["이미지"])
        else:
            print('Response error code : %d' % rescode)
            latitude = None
            longitude = None

'''
for x in docs:
    url = "https://jusoga.com/search?q={}".format(x["지역이름"])
    ##########
    response = requests.get(url)
    source = response.text
    soup = BeautifulSoup(source, "html.parser")
    a = soup.select_one("body > div.container > table > tbody > tr > td:nth-child(1) > a")
    try:
        list = a["href"]
    except TypeError as te:
        pass
    base_url = list
    response = requests.get(base_url)
    source = response.text
    # print(source)
    soup = BeautifulSoup(source, "html.parser")
    # 위도
    x = soup.select_one("body > div:nth-child(2) > table > tbody > tr:nth-child(5) > td")
    #print("위도",x.text)
    # 경도
    y = soup.select_one("body > div:nth-child(2) > table > tbody > tr:nth-child(6) > td")
    #print("경도",y.text)
    location.append([x.text, y.text])
'''

#지도 디폴트 셋팅
Y = 37.5722440
X = 126.9759352
main_location = (Y, X)
map_shic = folium.Map(location=main_location, zoom_start=8, title="map")
#print(location)
#print(location)
for x in range(len(location)):
    pop = folium.Popup(imglist[x]+'<br>'+str(name[x])+'<br>'+
                       "주소: "+info[x][0]+"<br>"+"전화번호: "+info[x][1], max_width=300)
    folium.Marker(location[x], popup=pop, icon=folium.Icon(color='blue')).add_to(map_shic)
map_shic.save("map.html")
webbrowser.open("map.html") #지도 html로 열기

#col.drop()
