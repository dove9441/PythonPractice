from selenium import webdriver
import time

input=input("상대 챔피언 입력 >> ")
browser=webdriver.Chrome("/Users/admin/Documents/visual studio code/Python/chromedriver_mac64_m1")
browser.get("https://www.op.gg/champion/statistics")
time.sleep(2)

champs=browser.find_elements_by_css_selector("div.champion-index__champion-item__name")
for i in champs:
    if i.text==input:
        i.click()
        break
time.sleep(2)

#카운터 매뉴 클릭하기
browser.find_element_by_css_selector("li.champion-stats-menu__list__item.champion-stats-menu__list__item--red.tabHeader").click() #여기서는 elements가 아닌 element임.
time.sleep(2)
#승률순 정렬
browser.find_element_by_css_selector("button.champion-matchup-sort__button.champion-matchup-sort__button--winrate").click()
browser.find_element_by_css_selector("button.champion-matchup-sort__button.champion-matchup-sort__button--winrate").click()
#카운터 챔프 크롤링
counter=browser.find_elements_by_css_selector("div.champion-matchup-list__champion>span:nth-child(2)") #:nth-child(N)은 자손의 N번째만 선택
for i in range(len(counter)):
    print("상대승률 ",i+1,"위: ",counter[i].text)
    
browser.close()