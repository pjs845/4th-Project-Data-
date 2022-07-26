from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pymongo import mongo_client

#몽고DB
host = "localhost"
port = 27017
client = mongo_client.MongoClient(host, port)
db = client["soobindb"]
col = db["rate"]  
col.drop()

path = "C:/PJS/PyAdvanced/day06_crawling/자료실/chromedriver.exe"
driver = webdriver.Chrome(path)

#페이지 크롤링
url = "https://map.kakao.com/"

import time
driver.get(url)

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#dimmedLayer").click()

for x in range(0, 10):
    driver.find_element(By.CSS_SELECTOR, "#view\.map > div.MapControlView > div.zoom_control.fold > div > button:nth-child(3)").click()
    time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "#search\.keyword\.bounds").click()
time.sleep(1)

el_search = driver.find_element("name", "q")
el_search.send_keys("캠핑장")

el_search.send_keys(Keys.ENTER)
time.sleep(0.1)
driver.find_element(By.CSS_SELECTOR, "#info\.search\.place\.more").click()
time.sleep(0.1)
driver.find_element(By.CSS_SELECTOR, "#info\.search\.page\.no1").click()
time.sleep(0.1)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

li = list()
num = 1
id = 1
for z in range(1,35):
    for x in range(1,17):
        name = soup.select_one("#info\.search\.place\.list > li:nth-child("+str(x)+") > div.head_item.clickArea > strong > a.link_name")
        rate = soup.select_one("#info\.search\.place\.list > li:nth-child("+str(x)+") > div.rating.clickArea > span.score > em")
        location = soup.select_one("#info\.search\.place\.list > li:nth-child("+str(x)+") > div.info_item > div.addr > p:nth-child(1)")
        review = soup.select_one("#info\.search\.place\.list > li:nth-child("+str(x)+") > div.rating.clickArea > a > em")
        try:
            #li.append([name["title"], rate.text, location.text])
            dict = {"_id":id, "캠핑장이름":name["title"], "장소":location.text, "평점":float(rate.text), "리뷰수":int(review.text)}
            col.insert_one(dict)
            print("z", z, "x", x, "num", num)
            id += 1
        except TypeError:
            pass
        except ValueError:
            dict = {"_id":id, "캠핑장이름":name["title"], "장소":location.text, "평점":rate.text, "리뷰수":int(review.text)}
            col.insert_one(dict)
            id += 1
    if z == 34:
        if num < 4:
            driver.find_element(By.CSS_SELECTOR, "#info\.search\.page\.no"+str(num+1)+"").click()
            time.sleep(1)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
        elif num == 4:
            break
    elif z < 34:
        if num < 5:
            driver.find_element(By.CSS_SELECTOR, "#info\.search\.page\.no"+str(num+1)+"").click()
            time.sleep(1)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
        elif num == 5:
            driver.find_element(By.CSS_SELECTOR, "#info\.search\.page\.next").click()
            time.sleep(1)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            num = 0
        num += 1
                
print(li)