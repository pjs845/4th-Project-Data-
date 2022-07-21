from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")

path = "C:/PJS/project/4차 Data/4th-Project-Data-/chromedriver.exe"
driver = webdriver.Chrome(path, options=options)
url = "https://jusoga.com/"
driver.get(url)

search = driver.find_element("name", "q")
search.send_keys("강원 고성군 토성면 신평골길 29-1")
search.send_keys(Keys.ENTER)
click = driver.find_element(By.XPATH, "/html/body/div[1]/table/tbody/tr/td[1]/a")
try:
    click.click()
except:
    pass
html = driver.page_source
# print(html)
soup = soup  = BeautifulSoup(html, "html.parser")

# 위도
x = soup.select_one("body > div:nth-child(2) > table > tbody > tr:nth-child(5) > td")
print("위도",x.text)
# 경도
y = soup.select_one("body > div:nth-child(2) > table > tbody > tr:nth-child(6) > td")
print("경도",y.text)


driver.quit()



