import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# 창 숨기는 옵션 추가
# options = webdriver.ChromeOptions()
# options.add_argument("headless")

# path = "C:\\Users\\kosmo\\Desktop\\3. python\\chromedriver_win32\\chromedriver.exe"
# driver = webdriver.Chrome(path) # , options=options
# url = "https://jusoga.com/"
# driver.get(url)
# search = driver.find_element("name", "q")
# search.send_keys("경기 포천시 소흘읍 광릉수목원로 932-2")
# search.send_keys(Keys.ENTER)


# html = driver.page_source

put = input("주소를 입력하세요: ")
url = "https://jusoga.com/search?q={}".format(put)
##########
response = requests.get(url)
source = response.text
soup = BeautifulSoup(source, "html.parser")
a = soup.select_one("body > div.container > table > tbody > tr > td:nth-child(1) > a")
list = a["href"]
sp = list.split("/")
num = sp[-2]
write = sp[-1]
base_url = "https://jusoga.com/b/{}/{}".format(int(num), str(write))
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



