import urllib.request as req
from bs4 import BeautifulSoup
f=open("알라딘중고샵.txt","w")

pagenum=1
while True:
    url="https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&KeyWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyLastWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&ViewRowCount=25&page={}".format(pagenum)
    code=req.urlopen(url)
    soup=BeautifulSoup(code,"html.parser")
    title=soup.select("a.bo3>b")
    price=soup.select("a.bo_used>b")
    if len(title)==0:
        break
    for i in range(len(title)): #반환되는 값들이 리스트 자료형임을 이용
        print(title[i].string, price[i].string)
        f.write(title[i].string+" , "+price[i].string+"\n")
    pagenum+=1
f.close