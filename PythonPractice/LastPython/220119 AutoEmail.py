import openpyxl
from email.mime.text import MIMEText
import smtplib
#아래 3개는 첨부파일 보낼 때 
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders



#메일 서버 로그인 (메일 사이트(네이버 메일 등)에서 확인)
server=smtplib.SMTP_SSL("smtp.naver.com",465) #네이버에 SSL필요라고 돼있음. 없으면 SSL 뺴기 ("서버주소",포트)
server.login("dotml386","penetration3752!") #아이디, 비번

book=openpyxl.load_workbook("./list.xlsx")
sheet=book.active
count=0
for row in sheet.rows: #한 행 전체씩을 가져옴
    if count%20==0:
        server.quit()
        server=smtplib.SMTP_SSL("smtp.naver.com",465) #네이버에 SSL필요라고 돼있음. 없으면 SSL 뺴기 ("서버주소",포트)
        server.login("dotml386","penetration3752!") #아이디, 비번
        
    if row[4].value=="X": #뽑아온 행의 4번째 열의 값을 가져옴
        continue
    date=row[0].value #0부터 시작임을 잊지 말자
    name=row[1].value #.value 없으면 커서만 거기로 이동한다고 보면 됨
    Eaddress=row[2].value 
    product=row[3].value
    title="{}님 결제 완료 안내 메일입니다.".format(name) #보낼 이메일 제목
    content="""
{}님 결제 완료 안내 내역입니다.
성함: {}
날짜: {}
상품: {}
""".format(name,name,date,product) #이메일 본문

#메일 보내기 (아직 for문 안이다!)
#server.sendmail("보내는 사람","받는 사람",msg.as_string())
    
    # msg=MIMEText(content, _charset="euc-kr")   #MIME은 전자우편 인터넷표준 포맷이다. #주석 단축키: 드래그후 커맨드+/
    # msg["From"]="dotml386@naver.com"
    # msg["To"]=Eaddress
    # msg["Subject"]=title #이러한 형식은 고정이다.
    CONTENT=MIMEMultipart()
    CONTENT["From"]="dotml386@naver.com"
    CONTENT["To"]=Eaddress
    CONTENT["Subject"]=title
    
    msg=MIMEText(content,_charset="euc-kr") #multipart 안에 MIMEText를 넣는것
    CONTENT.attach(msg)
    
    part=MIMEBase("application","octet-stream") #이 형식도 고정. 이진 파일을 보낼 때 사용
    part.set_payload(open("./testimg.jpg","rb").read()) #rb는 바이너리(이진)형식
    encoders.encode_base64(part)
    part.add_header("Content-Disposition","attachment; filename=testimg.jpg") #파일 이름 뺴고 고정
    CONTENT.attach(part)
    
    
    server.sendmail("dotml386@naver.com",Eaddress,CONTENT.as_string())
    
    print("{}님께 이메일을 전송했습니다.".format(name))
    count+=1

#too many command 오류 해결: count 변수로 중간중간 끊기
#어차피 안외워도 이 형식 자체가 고정이기 때문에 한 번만 작성해놓으면 나중에 복사해서 사용하면 된다.

    