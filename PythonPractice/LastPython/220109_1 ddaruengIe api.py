import requests
import json
import folium #pip3 install folium ,지도 생성을 통한 시각화에 필요
import os #파일 자동 실행을 위해 필요
from selenium import webdriver
import time


api_key="59487a4b6d646f763130367554575551"
url="http://openapi.seoul.go.kr:8088/{}/json/bikeList/1/20/".format(api_key)
data=requests.get(url)
result=json.loads(data.text)
#print(json.dumps(result,indent="\t")) #정리
rows=result["rentBikeStatus"]["row"] #인덱스 이름 잘 보고 특정부분 추출
latsum=0
longsum=0
for i in rows: #위도경도 평균 구해서 처음 지도 나타낼 때 이용 (아니면 print된 위도경도 대충 소숫점 3자리까지 넣으면 됨)
    lat=i["stationLatitude"]
    long=i["stationLongitude"]
    latsum+=float(lat)
    longsum+=float(long)
avelat=latsum/len(rows)
avelong=longsum/len(rows)


map=folium.Map(location=[avelat,avelong], zoom_start=13) #위도, 경도 입력 지도 나타내기
for i in rows:
    bikenum=i["parkingBikeTotCnt"]
    stationname=i["stationName"]
    lat=i["stationLatitude"]
    long=i["stationLongitude"]
    if int(bikenum)<3:
        color="red"
    elif 3<=int(bikenum)<=7:
        color="blue"
    elif int(bikenum)>7:
        color="green"
    #색변화를 위해 
    folium.Marker(location=[lat,long], popup=stationname, tooltip=bikenum,icon=folium.Icon(color=color)).add_to(map) #마커로 지도에 표시. 마커 클릭하면 정류소이름, 마우스만 올려놓으면 설치된 자전거 개수 나오게. map에 추가.
    map.save("./map.html") #파일 저장	
    print("정거소명: ",stationname,"    정거소 위치: 위도 ",lat,", 경도 ",long,"    사용 가능한 대수: ",bikenum)

filePath=os.path.abspath("./map.html") #파일의 절대 경로 반환	
#browser=webdriver.Chrome("/workspace/PythonPractice/LastPython/chromedriver")
#browser.get("file://"+filePath) #윈도우는 그냥 filePath 넣기 (또는 "file:///Users/admin/Documents/visual studio code/Python/map.html" 로 열기)
time.sleep(10)