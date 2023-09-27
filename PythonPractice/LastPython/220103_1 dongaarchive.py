#pip3 install requests
import requests
from bs4 import BeautifulSoup

sess=requests.session() #세션 만들기
data={
"idsave_value":"",
"errorChk":"" ,
"gourl": "https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19990103%26mode%3D19990103%2F0002132731%2F1",
"bid": "dove386",
"bpw": "dong08ju23",
}
h={
"Referer": "https://secure.donga.com/membership/login.php?gourl=https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19990103%26mode%3D19990103%2F0002132731%2F1",
}
sess.post("https://secure.donga.com/membership/trans_exe.php",headers=h,data=data) #headers에는 request headers, data에는 form data 넣기
code=sess.get("https://www.donga.com/archive/newslibrary/view?ymd=19990103&mode=19990103/0002132731/1") #urlopen이랑 같은 기능
soup=BeautifulSoup(code.text,"html.parser") #get함수 쓸때는 .text 붙이기
titlelist=soup.select("ul.news_list a")
for i in titlelist:
    print(i.string)
    newsURL="https://www.donga.com/archive/newslibrary/view?idx=19990103%2F"+i.attrs["onclick"].replace("javascript:getNewsArticle('19990103/","").replace("/1'); return false;","")+"%2F1"
    code=sess.get(newsURL)
    soup=BeautifulSoup(code.text,"html.parser")
    content=soup.select_one("div.article_txt")
    print(content.text.strip()) #.strip은 양옆 공백 삭제
    print() 