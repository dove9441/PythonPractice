import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
SCROLL_PAUSE_SEC=3

def scroll_down():
    global driver
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_SEC)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            time.sleep(SCROLL_PAUSE_SEC)
            new_height = driver.execute_script("return document.body.scrollHeight")

            try:
                driver.find_element_by_class_name("mye4qd").click()
            except:

               if new_height == last_height:
                   break


        last_height = new_height





keyword=input("Enter keyword>> ")
url="https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiVtdGWyfb0AhUWslYBHa9vAqAQ_AUoAXoECAIQAw&biw=1680&bih=914&dpr=2".format(keyword)
driver=webdriver.Chrome("/Users/admin/Documents/visual studio code/Python/chromedriver_mac64_m1")
driver.get(url)
scroll_down()
source=driver.page_source
soup=BeautifulSoup(source,"html.parser")
imgs=soup.find_all("img",attrs={"class":"rg_i Q4LuWd"})
print('number of img tags: ', len(imgs))


n = 1
for i in imgs:

    try:
        imgUrl = i["src"]
    except:
        imgUrl = i["data-src"]
        
    with urllib.request.urlopen(imgUrl) as f:
        with open('/Users/admin/Documents/visual studio code/Python/catimg/' + keyword + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)

    n += 1
