from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par

keyword=input("Enter keyword >> ")
encoded=par.quote(keyword) #한글을 변환
url="https://www.joongang.co.kr/search/news?keyword={}".format(encoded)
headers=req.Request(url,headers={"User-Agent":"Mozilla/5.0"})
code=req.urlopen(headers)
soup=BeautifulSoup(code,"html.parser")
title=soup.select("ul.story_list h2.headline>a")

for i in range(len(title)):
    print("제목: ",title[i].text)
    print("링크: ",title[i].attrs["href"]) #속성명으로 링크주소 찾기
    news_code=req.urlopen(title[i].attrs["href"])
    news_soup=BeautifulSoup(news_code,"html.parser")
    news=news_soup.select_one("div#article_body")
    print("본문: ",news.text.strip().replace("  ","")) #.strip은 양쪽의 공백을 삭제한다. .replace는 "  "를 ""로 교체
    print()


