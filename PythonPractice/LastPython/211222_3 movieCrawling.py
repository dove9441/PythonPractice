import urllib.request as req #req가 인수 이름
from bs4 import BeautifulSoup

#서버로부터 html 코드 받기
code=req.urlopen("http://www.cgv.co.kr/movies/")
#print(code.read())
soup=BeautifulSoup(code,"html.parser")
#print(soup)
#title=soup.select_one("strong.title") #태그명.속성값 (.이 class 속성명을 의미, 속성명이 class가 아닌 id라면 태그명#속성값)
#print(title.string)
#title=soup.select_one("a>strong.title") #태그명 a의 자손 select_one은 맨 위의 하나만 가져옴. select는 모든 것을 리스트 자료형으로 가져옴.
#title=soup.select("div.box-contents strong.title") #div 태그명의 box-contents 속성값을 가진 class 속성명을 가진 조부모의 strong 태그명 class 속성명 title 속성값 자손
#css 속성: '.' clsss 속성 '#': id 속성 ' ': 조부모-후손 관계 '>': 부모-자손 관계
title=soup.select("div.sect-movie-chart strong.title")
for i in title:
    print(i.string)