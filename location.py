from pymongo import mongo_client
import urllib.request
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://address.dawul.co.kr/'
response = requests.get(url)
source = response.text
soup = BeautifulSoup(source, "html.parser")

