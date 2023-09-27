import urllib.request as req
from bs4 import BeautifulSoup
import operator


input=input("상대 챔프 입력 >> ")

headers=req.Request("https://www.op.gg/champion/statistics",headers={"Accept-Language":"ko-KR"}) #한글로 요청받기 (잘 모름)

url=req.urlopen(headers)
soup=BeautifulSoup(url,"html.parser")
champlist=soup.select("div.champion-index__champion-list>div")
for i in champlist:
    if i.attrs["data-champion-name"]==input:
        a=i.select_one("a") #태그명 a 안에 url이 있음 중요!! 이렇게 안해주고 herf 갖다박으면 오류남
        champUrl="https://www.op.gg"+a.attrs["href"] #태그명 a 안 herf 속성값으로 url이 있음 , 미완성된 url이므로 앞에 추가해줌
        break;
print(champUrl)



headers=req.Request(champUrl,headers={"Accept-Language":"ko-KR"})
code=req.urlopen(headers)
soup=BeautifulSoup(code, "html.parser")
#여기까지 챔프의 웹페이지 html을 받음 
counterTab=soup.select_one("li.champion-stats-menu__list__item.champion-stats-menu__list__item--red.tabHeader")
a=counterTab.select_one("a")
counterURL="https://www.op.gg"+a.attrs["href"]

#여기까지 카운터탭 들어가서의 웹페이지 url을 받음

headers=req.Request(counterURL,headers={"Accept-Language":"ko-KR"})
code=req.urlopen(headers)
soup=BeautifulSoup(code,"html.parser")
countername=soup.select("div.champion-matchup-list__champion>span:nth-child(2)")
counterwinrate=soup.select("div.champion-matchup-list__champion>span:nth-child(3)")

countername2=[] #(태그제거)
for i in range(len(countername)):
    temp=countername[i].string
    countername2.append(temp)


counterwinrate2=[]
for i in range(len(counterwinrate)):
    temp=counterwinrate[i].string
    counterwinrate2.append(temp)

afterReplace=[] #정렬하기 위해 %제거
for i in counterwinrate2:
    temp=i.string.replace("%","")
    afterReplace.append(temp)

afterreplace2=[] #쓸데없는부분 제거
for i in afterReplace:
    temp=i.replace("\t","").replace("\n","")
    afterreplace2.append(temp)
        

dic=dict(zip(countername2,afterreplace2)) #정렬
sdict=sorted(dic.items(),key=operator.itemgetter(1))
n=1
for i in sdict:
    print("상대승률 ",n,"위 : ",i,"%")
    n+=1




