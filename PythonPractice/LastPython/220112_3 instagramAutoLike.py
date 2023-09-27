from selenium import webdriver
import time
import selenium
import random


hashtag=input("Enter hashTag to search >> ")
browser=webdriver.Chrome("/Users/admin/Documents/visual studio code/Python/chromedriver_mac64_m1")
browser.get("https://www.instagram.com/?hl=ko")
time.sleep(4)
id=browser.find_element_by_css_selector("input[name=""username""]") #이런 형식의 방법도 알기. 태그명[속성명="속성값"]
id.send_keys("01056187952")
pw=browser.find_element_by_css_selector("input[name=""password""]")
pw.send_keys("penetration3752!")
browser.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF").click()
time.sleep(3)
TagURL="https://www.instagram.com/explore/tags/{}/".format(hashtag)
browser.get(TagURL)
time.sleep(5)
browser.find_element_by_css_selector("div._9AhH0").click()
time.sleep(3)

while True:
    like=browser.find_element_by_css_selector("span.fr66n>button.wpO6b")
    valueElement=browser.find_element_by_css_selector("span.fr66n>button.wpO6b svg[aria-label]") #like의 속성값을 가져올 수 있으면 더 좋으나 내부 속성값이기 때문에 따로 지정해야 함
    value=valueElement.get_attribute("aria-label") #속성명의 속성값 가져오기
    print(value)
    next=browser.find_element_by_css_selector("div.l8mY4.feth3>button.wpO6b")
    if value=="좋아요":
        like.click()
        time.sleep(random.randint(2,5)+random.random())
        next.click()
        time.sleep(random.randint(2,5)+random.random())
    elif value=="좋아요 취소":
        next.click()
        time.sleep(random.randint(2,5)+random.random())
        