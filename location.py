import numpy as np
import pandas as pd
from urllib.request import urlopen
from urllib import parse
from urllib.request import Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json

#naver map api key
client_id = 'k3y82rodr8';    # 본인이 할당받은 ID 입력
client_pw = '6STyg87wDH81UANRy4ameDXDRE0Vxie1w09HfYdU';    # 본인이 할당받은 Secret 입력

api_url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='


# 네이버 지도 API 이용해서 위경도 찾기
geo_coordi = []     
for x in range(0,1):
    add = "경남 남해군 미조면 송정리 1379 외2"
    add_urlenc = parse.quote(add)  
    url = api_url + add_urlenc
    request = Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_pw)
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
        else:
            print('Response error code : %d' % rescode)
            latitude = None
            longitude = None

    geo_coordi.append([latitude, longitude])


np_geo_coordi = np.array(geo_coordi)
pd_geo_coordi = pd.DataFrame({"도로명": "경남 남해군 미조면 송정리 1379 외2",
                              "위도": np_geo_coordi[:, 0],
                              "경도": np_geo_coordi[:, 1]})
print(pd_geo_coordi)