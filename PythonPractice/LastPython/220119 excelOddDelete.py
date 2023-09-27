import openpyxl
import pandas  #pip3 install pandas 추가적으로 install xlrd도 하기
#pandas는 대량 데이터 가공에 유용
#openpyxl은 엑셀의 모든 기능을 사용 가능하다	

df=pandas.read_excel("./엑셀데이터/전자기기매출액.xlsx") #pandas(Pathon Data Analysis Library는 데이터프레임이라는 자료형으로 파일을 가져옴)
print(df[: : 2]) #df[A:B:C] A부터 B행까지 C번쨰 행개씩 가져옴
#쓸데없는 행이 사라졌다.
df[::2].to_excel("./엑셀데이터/전자기기매출액_짝수행만.xlsx") #저장

#아주 간편하다
df[::2].to_excel("./엑셀데이터/전자기기매출액_짝수행_인덱스X.xlsx",index=None)  #1열 인덱스번호 없음