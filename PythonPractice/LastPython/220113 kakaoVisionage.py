import requests
from requests.api import head
import json

REST_API="e679a168d0fb8924452617aa297a4b1d"
RequestURL="https://dapi.kakao.com//v2/vision/face/detect"
headers={'Authorization': 'KakaoAK {}'.format(REST_API)}    

files = { 'image' : open("./testimg04.jpeg", 'rb')}
result=requests.post(RequestURL,headers=headers,files=files)
result.status_code
print(result.json())
dicresult=json.loads(result.text) #result.text처럼 .text를 꼭 써야 한다

print("추정 나이:",dicresult["result"]["faces"][0]["facial_attributes"]["age"]) #리스트 속 딕셔너리 속 리스트..등 분석 조심
#print(dicresult)