api_id="snfr5d9f5s"
api_pw="I5dYPlWWdjF2tIMPJDipul1okaSIbPAjLzBUNyhJ"

#음성 파일을 텍스트로 변환해줌 (AI 이용)
import sys
import requests
client_id = api_id
client_secret = api_pw
lang = "Kor" # 언어 코드 ( Kor, Jpn, Eng, Chn )
url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
data = open('/Users/admin/Documents/visual studio code/Python/음성파일예시.mp3', 'rb')
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/octet-stream"
}
response = requests.post(url,  data=data, headers=headers)
rescode = response.status_code
if(rescode == 200):
    print (response.text)
else:
    print("Error : " + response.text)
