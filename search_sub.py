import requests
from bs4 import BeautifulSoup

print(">>주소를 입력 해 주세요<<")
put = input()
url = "https://jusoga.com/search?q={}".format(put)
####################################################
response = requests.get(url)
source = response.text
soup = BeautifulSoup(source, "html.parser")
a = soup.select_one("body > div.container > table > tbody > tr > td:nth-child(1) > a")
list = a["href"]
base_url = list
response = requests.get(base_url)
source = response.text
soup = BeautifulSoup(source, "html.parser")

# 위도
x = soup.select_one("body > div:nth-child(2) > table > tbody > tr:nth-child(5) > td")
x = float(x.text)
# 경도
y = soup.select_one("body > div:nth-child(2) > table > tbody > tr:nth-child(6) > td")
y = float(y.text)
print("위도:", x)
print("경도:", y)
