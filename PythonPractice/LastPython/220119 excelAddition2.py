import pandas



writer=pandas.ExcelWriter("./엑셀데이터/장사시설(장례식장)현황합치기.xlsx") #ExcelWriter는 기능을 더해줌
for year in range(2017,2020):
    df=pandas.read_excel("./엑셀데이터/장사시설현황_2017년_2020년/{}년 장사시설 현황/전국장사시설현황.xlsx".format(year),sheet_name="장례식장 시설정보") #시트네임 지정
    df[["시설명","주소"]].to_excel(writer,sheet_name="{}년".format(year),index=None)   #한 개면 대괄호 하나, 두 개 이상이면 대괄호 두 개로 리스트 자료형을 전달. 시트이름으로 따로 지정해서 저장 가능
writer.save()