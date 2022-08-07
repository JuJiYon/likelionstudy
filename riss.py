from selenium import webdriver
from bs4 import BeautifulSoup 
import os, sys, time

# 웹페이지 자동 접속하기와 응용
# ("/Users/유저명/py_temp/chromedriver.exe") # 맥
driver = webdriver.Chrome("C:/Users/JY/py_temp/chromedriver.exe")
time.sleep(3)
driver.get("http://www.riss.kr/")


# 팝업창 갯수를 모를 경우 모두 닫기
time.sleep(2)
main = driver.window_handles 

for handle in main: 
    if handle != main[0]: 
        driver.switch_to.window(handle) 
        driver.close()

# 원래 창으로 돌아가기
driver.switch_to.window(driver.window_handles[0])


# 창 크기 최대화
time.sleep(2)
driver.maximize_window()

# 엘리먼트 찾아 제어하기
time.sleep(2)
driver.find_element_by_id("query").send_keys("빅데이터"+"\n")

time.sleep(5)
driver.find_element_by_link_text("학위논문").click()
# 웹데이터 수집하기
soup = BeautifulSoup(driver.page_source, 'html.parser') #페이지 전체, 분석
content = soup.find('div','srchResultListW').find_all('li')

for i in content : 
    print(i.get_text())
    print("\n")

driver.close()