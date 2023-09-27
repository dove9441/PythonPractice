from selenium import webdriver
import time
import selenium

option=webdriver.ChromeOptions()
option.add_argument("headless")
browser=webdriver.Chrome("/Users/admin/Documents/visual studio code/Python/chromedriver_mac64_m1")  #크롬창 안뜨게 설정

browser.get("https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net")
id=browser.find_element_by_css_selector("input#id_email_2")#label 태그명과 input 태그명이 나올 텐데 label은 회색글자를 의미함. input을 실제 사용해야 한다. (값 입력은 무조건 input)
id.send_keys("naver.com875@gmail.com")
password=browser.find_element_by_css_selector("input#id_password_3")
password.send_keys("dongju357982!")
browser.find_element_by_css_selector("button.btn_g.btn_confirm.submit").click() #click()으로 클릭
time.sleep(2) #딜레이 주기

browser.get("https://mail.daum.net/") #이메일함으로 이동
#browser.find_elements_by_css_selector("a.btn_login").click()
time.sleep(2)
title=browser.find_elements_by_css_selector("strong.tit_subject")
for i in title:
    print(i.text)

browser.close()