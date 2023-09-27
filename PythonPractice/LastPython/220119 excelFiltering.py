import pandas as pd
df=pd.read_excel("./엑셀데이터/아파트분양가격.xlsx")
print(df[df["분양가격"]>=3000]) #문법이 이렇다.
print(df[(df["지역명"]=="서울")&(df["분양가격"]>=4000)])