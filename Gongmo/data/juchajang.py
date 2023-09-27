import pandas as pd
import folium
import os
import numpy as np
import math


df = pd.read_csv('./Parkingloc.csv')
nparr = df.to_numpy()
map=folium.Map(location=[37.497225,127.027375], zoom_start=18)
print(nparr)
for row in nparr:
    if math.isnan(row[0]) or math.isnan(row[1]):
        continue
    else:
        lat=row[0]
        long=row[1]
        folium.Marker(location=[lat,long], popup="0", tooltip="0", icon=folium.Icon(color="green")).add_to(map)
        #print("위도 : {}, 경도 : {} 추가됨".format(lat,long))
        
print('map.html을 저장 중입니다 ...')
map.save("./ParkingLotmap.html")
print('파일 저장 완료')
    
    
    
# gc.collect()
# map=folium.Map(location=[37.497225,127.027375], zoom_start=18)
# print("로드 완료 데이터 추가 중 ...")
# for row in nparr:#df.itertuples():
#     #num=row[0]
#     date=row[0]
#     lat=row[1]
#     long=row[2]
#     #folium.Marker(location=[lat,long], popup=date, tooltip=date, icon=folium.Icon(color="green")).add_to(map)
#     folium.Circle(location = [lat,long], radius = 10, popup=date).add_to(map)
#    # print(" 일시 : {}, 위도 : {}, 경도 : {} 추가됨".format(date,lat,long))
# del nparr
# gc.collect()
# print('map.html을 저장 중입니다 ...')
# map.save("./map.html")
# print('파일 저장 완료')