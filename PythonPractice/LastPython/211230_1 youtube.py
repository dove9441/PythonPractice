from selenium import webdriver 
import time
from selenium.webdriver.common.keys import Keys

option=webdriver.ChromeOptions()
option.add_argument("headless")
browser=webdriver.Chrome("/Users/admin/Documents/visual studio code/Python/chromedriver_mac64_m1",options=option)
browser.get("https://www.youtube.com/watch?v=6JOc3ig9w4A")
time.sleep(2)
# 맨 처음에 스크롤 조금 내려주기
#browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN) #아무 css요소를 앞에다 붙여줘야 작동함. 모든 웹사이트에 있는 태그명 html을 이용
#맨 처음에 스크롤 끝까지 내려주기
browser.find_element_by_css_selector("html").send_keys(Keys.END)
time.sleep(3)

#댓글 크롤링
comments=browser.find_elements_by_css_selector("yt-formatted-string#content-text") #또는 태그명 생략해서 #content-text라고만 써도 됨 #elements여야지 list형이다!! s 주의

i=0
while True:
    try:
        print(comments[i].text)
    except:
        print("compeleted.")
        break
    i+=1
    #20개마다 스크롤하기(하지만 그보다 적게)(css선택자 검색으로 몇개마다인지 확인)
    if (i%15)==0:
        browser.find_element_by_css_selector("html").send_keys(Keys.END)
        time.sleep(4)
        comments=browser.find_elements_by_css_selector("yt-formatted-string#content-text") #내리고 다시 크롤링 (이전 크롤링 결과 포함, i는 유지되므로 중복출력 안됨.)
        
browser.close()
#주의! 실행할 때 크롬창 보이게 해놓고 작업해야지 안밀리고 제대로 된다. 아니면 headless 옵션 쓰든지