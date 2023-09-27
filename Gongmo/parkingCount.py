import pandas as pd
import os
import numpy as np
from haversine import haversine 
import time
import csv



start=time.time()

parkingdf = pd.read_csv('./data/Parkingloc.csv')
mindf = pd.read_csv('./data/2101.csv')
print("dataframe loaded.")

# startPoint = "기준 주차장 위치"
# endPoint = ""
# distance = haversine(startPoint,endPoint)
# print(distance)

minnp = mindf.to_numpy()
parkingnp = parkingdf.to_numpy()

cntarr=[]

for i in range(len(mindf)):
    cnt=0
    STlat = minnp[i][1]
    STlong = minnp[i][2]
    startPoint = (STlat, STlong)
    
    for j in range(len(parkingdf)):
        DTlat = parkingnp[j][0]
        DTlong = parkingnp[j][1]
        endPoint = (DTlat, DTlong)
        distance = haversine(startPoint,endPoint)
        #print("{}, {}km".format(j,distance))
        if distance<=0.5:
            cnt+=1
    cntarr.append(cnt)
    print("2101 index {} 추가됨 cnt : {}.".format(i,cnt))
    end=time.time()
    print(f"{end - start:.5f} sec")








# for i in range(len(parkingdf)):
#     cnt=0
#     STlat = parkingnp[i][0]
#     STlong = parkingnp[i][1]
    
#     startPoint = (STlat, STlong)
    
#     for j in range(len(mindf)):
#         DTlat = minnp[j][1]
#         DTlong = minnp[j][2]
#         endPoint = (DTlat, DTlong)
#         distance = haversine(startPoint,endPoint)
#         #print("{}, {}km".format(j,distance))
#         if distance<=0.5:
#             cnt+=1
#     cntarr.append(cnt)
#     print("Parkingloc index {} 추가됨 cnt : {}.".format(i,cnt))
#     end=time.time()
#     print(f"{end - start:.5f} sec")
    



with open('./data/count.csv','w') as file :

    write = csv.writer(file)
    write.writerow(cntarr)
end=time.time()
print("end")
print(f"{end - start:.5f} sec")

    
    
    
    
