#pip3 install requests
import requests
import json


api_key="c96a3488558ef58d5300df6bdb89c571"
URL="http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format("Seoul",api_key) #앞에 http:// 붙이기
data=requests.get(URL)
#print(data.text["coord"]) #text 꼭 쓰기, json 형식으로 받아오므로 import json 하고 다른 출력방식(아래) 사용
result=json.loads(data.text) #s 주의. json을 딕셔너리 자료형을 변환시켜줌
print("도시 이름: ",result["name"])
print("현재 날씨: ",result["weather"][0]["main"]) #리스트 안에 딕셔너리가 있는 것이었음.
print("최저/최고 기온: ",round(result["main"]["temp_min"]-273.15,2),"(C)/",round(result["main"]["temp_max"]-273.15,2),"(C)")