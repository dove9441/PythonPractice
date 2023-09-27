from bs4 import BeautifulSoup
import urllib.request as req

url="https://www.instagram.com/sang_or_/following/"
headers=req.Request(url,headers={"User-Agent":"Mozilla/5.0"})
code=req.urlopen(headers)
soup=BeautifulSoup(code,"html.parser")
followings_id=soup.select('_aacl _aaco _aacw _aacx _aad7 _aade')
following_name=soup.select('_aaeq')


for i in range(len(followings_id)):
    print(followings_id[i].text+'\n')
