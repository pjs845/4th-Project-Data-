import webbrowser
import folium
from bs4 import BeautifulSoup
import requests



url = "https://jusoga.com/search?q={}".format("경상북도 문경시 농암면 율수리")
##########
response = requests.get(url)
source = response.text
soup = BeautifulSoup(source, "html.parser")
a = soup.select_one("body > div.container > table > tbody > tr > td:nth-child(1) > a")
try:
    list = a["href"]
    base_url = list
    response = requests.get(base_url)
    source = response.text
    # print(source)
    soup = BeautifulSoup(source, "html.parser")
    # 위도
    x = soup.select_one("body > div:nth-child(2) > table > tbody > tr:nth-child(5) > td")
    print("위도",x.text)
    # 경도
    y = soup.select_one("body > div:nth-child(2) > table > tbody > tr:nth-child(6) > td")
    print("경도",y.text)

    #지도 디폴트 셋팅
    Y = 37.5722440
    X = 126.9759352
    main_location = (Y, X)
    map_shic = folium.Map(location=main_location, zoom_start=8, title="map")
    #print(location)
    #for x in range(len(location)):
    folium.Marker([x.text, y.text], icon=folium.Icon(color='blue')).add_to(map_shic)
    map_shic.save("map.html")
    webbrowser.open("map.html") #지도 html로 열기
except TypeError:
    print("주소가 없습니다.")

