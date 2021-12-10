# 라이브러리 불러오기
from selenium import webdriver
import time

url = 'http://0.0.0.0:5000/'

# 드라이버 연결
driver = webdriver.Chrome('/Users/hwangjihye/github/239band/chromedriver')
# 웹사이트 이동
driver.get(url)
#driver.implicitly_wait(10)

# # 원하는 요소(element)를 찾습니다. 이 경우에는 검색창입니다.
# search_box = driver.find_element_by_id('headerSearchKeyword')
# # 다음과 같은 동작을 하는 액션 체인을 만들었습니다.
# # 검색창을 찾고 '아이스크림'이라는 검색어를 입력한 뒤 Enter를 입력합니다.
# actions = webdriver.ActionChains(driver).send_keys_to_element(search_box, '아이스크림').send_keys(Keys.ENTER)
# # 체인을 실행합니다.
# actions.perform()

#driver.refresh()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div/a[3]').click()

