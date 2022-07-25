from pymongo import mongo_client
import webbrowser
import folium
from urllib.request import urlopen
from urllib import parse
from urllib.request import Request
from urllib.error import HTTPError
import json

id = 1
#몽고DB
host = "localhost"
port = 27017
client = mongo_client.MongoClient(host, port)
db = client["soobindb"]
col = db["site"]  
    
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

