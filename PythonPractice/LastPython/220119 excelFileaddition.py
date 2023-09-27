import pandas

df_merge=pandas.DataFrame()
# df1=pandas.read_excel("./엑셀데이터/2017년_광고비_LG전자.xlsx")
# df2=pandas.read_excel("./엑셀데이터/2017년_광고비_현대자동차.xlsx")
# df3=pandas.read_excel("./엑셀데이터/2017년_광고비_삼성전자.xlsx") 로 할 수도 있지만

company=["LG전자","삼성전자","현대자동차"]
for i in company:
    df=pandas.read_excel("./엑셀데이터/2017년_광고비_{}.xlsx".format(i))
    df.set_index("date",inplace=True) #인덱스를 읽은 파일의 "date" 열로 지정하겠다 inplce는 내부적으로 변경사항을 작용한다.
    df_merge[i]=df["total"] #열 기준이다
df_merge.to_excel("./엑셀데이터/2017광고비total.xlsx")