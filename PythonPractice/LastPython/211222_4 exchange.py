import urllib.request as req
from bs4 import BeautifulSoup

url=req.urlopen("https://finance.naver.com/marketindex/")
soup=BeautifulSoup(url,"html.parser")
rate=soup.select("div.market1 span.value")
for i in rate:
    print(i.string)