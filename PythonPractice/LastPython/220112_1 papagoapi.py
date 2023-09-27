api_id="5zzupa_lqKZUtDNVNmy1"
api_pw="3EE7yXCL0h"

import urllib.request as req
from bs4 import BeautifulSoup
import re
import os
import sys
import urllib.request
import json

    #에러 1. 한번에 5000개 글자만 번역 가능하기 떄문에 오류가 남. 따라서 위처럼 글자수 잘라서 해결
    #에러 2. 무료 api를 통한 하루 번역 단어 개수는 10000개. 하루 허용치 초과해서 오류.
    
keyword = input("영어로 키워드 입력 >> ")
page_num = 1
while True:
    url = "http://www.koreaherald.com/search/index.php?q={}&sort=1&mode=list&np={}&mp=1".format(keyword, page_num)
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    articles = soup.select("ul.main_sec_li > li > a")
    if len(articles) == 0:
        break
    for i in articles:
        title = i.select_one("div.main_l_t1")
        print("제목 :", title.text)
        link = "http://www.koreaherald.com" + i.attrs["href"]
        code_news = req.urlopen(link)
        soup_news = BeautifulSoup(code_news, "html.parser")
        contents = soup_news.select_one("div#articleText")
        # 데이터 가공
        result = re.sub(r'(\\[x]..)|(\\r)|(\\n)|(\\t)|(\(Yonhap\))', "", contents.text.strip())
        
        if len(result)>5000:
            result=result[0:5000]
        
        
        client_id = api_id # 개발자센터에서 발급받은 Client ID 값
        client_secret = api_pw # 개발자센터에서 발급받은 Client Secret 값
        encText = urllib.parse.quote(result)
        data = "source=en&target=ko&text=" + encText #출발언어, 도착언어 설정
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            result2=response_body.decode('utf-8')
            dicresult=json.loads(result2) #이렇게 딕셔너리로 바꿔야 인덱스 이름으로 찾아올 수 있음. load 하면 오류난다 s 꼭 붙이기
        else:
            print("Error Code:" + rescode)

        print(dicresult["message"]["result"]["translatedText"])
        print()
    page_num += 1
    
    


 


    

    
