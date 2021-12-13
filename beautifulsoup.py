import requests
from bs4 import BeautifulSoup
url = "https://www.daum.net/"

req = requests.get(url)
print(req)		 # get은 단순히 응답코드만 가져옵니다.
print(req.text)