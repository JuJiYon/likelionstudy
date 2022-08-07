from selenium import webdriver
from bs4 import BeautifulSoup 
import os, sys, time

# 웹페이지 자동 접속하기와 응용
# ("/Users/유저명/py_temp/chromedriver.exe") # 맥
driver = webdriver.Chrome("C:/Users/JY/py_temp/chromedriver.exe")
time.sleep(3)
driver.get("http://www.naver.com/")


# 팝업창 갯수를 모를 경우 모두 닫기
time.sleep(2)
main = driver.window_handles 



# 원래 창으로 돌아가기
driver.switch_to.window(driver.window_handles[0])


# 창 크기 최대화
time.sleep(2)
driver.maximize_window()

# 엘리먼트 찾아 제어하기
time.sleep(2)
driver.find_element_by_id("query").send_keys("빅데이터"+"\n")


time.sleep(5)
driver.find_element_by_link_text("VIEW").click()
driver.find_element_by_xpath('//*[@id="snb"]/div[1]/div/div[1]/a[2]').click()

# 웹데이터 수집하기
soup = BeautifulSoup(driver.page_source, 'html.parser') #페이지 전체, 분석
content = soup.find('ul',class_='lst_total').find_all('li')

for i in content : 
    print(i.get_text().replace("문서 저장하기  Keep에 저장 Keep 바로가기  ","").strip())
    # strip: 공백제거
    print("\n")

# 표준출력방향을 변경해서 파일로 저장

orig_stdout = sys.stdout
file = open("C:/Users/JY/py_temp/naver.txt" , 'a' , encoding='UTF-8')
sys.stdout = file  #모니터에 출력하지 말고 file 에 출력해라

for i in content :
    print(i.get_text().replace("문서 저장하기 Keep에 저장 Keep 바로가기",""))

file.close()    
sys.stdout = orig_stdout  #원래대로 변경 - 다시 화면에 출력시켜라    

print('요청하신 데이터 수집 작업이 정상적으로 완료되었습니다')


time.sleep(2)
driver.close()