import requests
import json
from haversine import haversine #하버 사인 공식 
from bs4 import BeautifulSoup



encode_key="RuCfZXy%2BiEdviWdGSGLKJg1o%2Fv7xLkiwQq2tHqLj%2FO4tw8XT23wo6bBEidHvbqOrPutxuWzhcavJuu6zBHWTsw%3D%3D"
decode_key="RuCfZXy+iEdviWdGSGLKJg1o/v7xLkiwQq2tHqLj/O4tw8XT23wo6bBEidHvbqOrPutxuWzhcavJuu6zBHWTsw=="

url="http://api.data.go.kr/openapi/tn_pubr_prkplce_info_api?serviceKey={}&pageNo=0&numOfRows=100&type=json".format(decode_key)

locURL="&latitude={}&longitude={}"


# startPoint = "기준 주차장 위치"
# endPoint = ""
# distance = haversine(startPoint,endPoint)
# print(distance)



# url = 'http://api.data.go.kr/openapi/tn_pubr_prkplce_info_api'
# params ={'serviceKey' : encode_key, 
#          'pageNo' : '0', 
#          'numOfRows' : '100', 
#          'type' : 'xml', 
#          'prkplceNo' : '', 
#          'prkplceNm' : '', 
#          'prkplceSe' : '', 
#          'prkplceType' : '',
#          'rdnmadr' : '', 
#          'lnmadr' : '', 
#          'prkcmprt' : '', 
#          'feedingSe' : '', 'enforceSe' : '', 
#          'operDay' : '', 'weekdayOperOpenHhmm' : '', 
#          'weekdayOperColseHhmm' : '', 
#          'satOperOperOpenHhmm' : '',
#          'satOperCloseHhmm' : '', 
#          'holidayOperOpenHhmm' : '', 
#          'holidayCloseOpenHhmm' : '', 
#          'parkingchrgeInfo' : '', 
#          'basicTime' : '',
#          'basicCharge' : '', 
#          'addUnitTime' : '', 
#          'addUnitCharge' : '', 
#          'dayCmmtktAdjTime' : '',
#          'dayCmmtkt' : '', 
#          'monthCmmtkt' : '',
#          'metpay' : '', 'spcmnt' : '', 
#          'institutionNm' : '',
#          'phoneNumber' : '', 
#          'latitude' : '', 
#          'longitude' : '',
#          'referenceDate' : '',
#          'instt_code' : '' }


response = requests.get(url)
print(response.content)