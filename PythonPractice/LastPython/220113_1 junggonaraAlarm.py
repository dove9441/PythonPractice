# 네이버 셀레니움 로그인
from selenium import webdriver
import pyperclip    # pip install pyperclip 입력하여 모듈 설치!
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
import os
import warnings
warnings.filterwarnings('ignore')

def input_id_pw(browser, css, user_input):
    pyperclip.copy(user_input)  # input을 클립보드로 복사
    browser.find_element_by_css_selector(css).click()  # element focus 설정
    # ActionChains(browser).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()  # 윈도우 : Ctrl+V 전달
    ActionChains(browser).key_down(Keys.LEFT_SHIFT).key_down(Keys.INSERT).key_up(Keys.LEFT_SHIFT).key_up(Keys.INSERT).perform()  # 맥 : shift+insert 전달
    time.sleep(1)


browser = webdriver.Chrome("/Users/admin/Documents/visual studio code/Python/chromedriver_mac64_m1")

browser.get("https://nid.naver.com/nidlogin.login")

input_id_pw(browser, "#id", "dotml386")
time.sleep(1)
input_id_pw(browser, "#pw", "penetration3752!")
time.sleep(1)

browser.find_element_by_css_selector("button.btn_login").click()
time.sleep(2)
browser.get("https://cafe.naver.com/joonggonara?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10050146%26search.boardtype=L")
time.sleep(2)
#선택자 맞는데 크롤링 안되면 뭐다? 프레임이다!
browser.switch_to.frame(browser.find_element_by_css_selector("iframe#cafe_main")) # 프레임 전환
title=browser.find_elements_by_css_selector("a.article")
for i in title:
    print(i.text)
    

#과거의 게시물 제목이 들어있는 메모장 파일 불러오기
newone=0
try:
    f=open("./종고나라.txt","r")
    ref=f.readlines()
except: #파일 없으면 새로 생성 근데 이상하게 계속 except구문이 실행된다. 아래를 w에서   
    f=open("./중고나라.txt","a")
    ref=[]

for i in title: 
    if not (i.text+"\n") in ref: #최신의 글이라면
        f=open("./중고나라.txt","a")
        f.write(i.text+"\n")
        if "아이패드" in i.text:
            newone+=1
f.close()
print("-------------------------------------------------")
print("{} 관련 글이 {}개 올라왔습니다.".format("아이패드",newone))

browser.close()


from twilio.rest import Client #pip3 install twilio
phoneNumber="+17156036428"
SID="AC0ff8e9e6eade34ae95914e65399219fb"
AUTHTOKEN="0e0e11c016cd7253ebba4be3e8b0cdf3"



if newone>=1:
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid =SID
    auth_token =AUTHTOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                        body="{} 관련 글이 {}개 올라왔습니다. https://cafe.naver.com/joonggonara".format("아이패드",newone),
                        from_='+17156036428',
                        to='+821056187952'
                    )

    print(message.sid)
