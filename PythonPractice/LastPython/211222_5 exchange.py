import urllib.request as req
from bs4 import BeautifulSoup



print("1.USD   2.JPY    3.EUR  4.CNY")
x=int(input("select>> "))
unit=["USD","JPA","EUR","CNY"]
cost=int(input("Enter money (%s)>> " %unit[x-1]))

url=req.urlopen("https://finance.naver.com/marketindex/")
soup=BeautifulSoup(url,"html.parser")
rate=soup.select("div.market1 span.value")
#이러면 rate 리스트는 ["미국", "일본","유럽","중국"] 이렇게 됨.
price=float(rate[x-1].string.replace(",",""))
if x==2:
    print("%s(₩)" %(round((price*cost/100),3)))
else:
    print("%s(₩)" %round((price*cost),3))
