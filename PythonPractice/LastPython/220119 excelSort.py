import pandas as pd
df=pd.read_excel("./엑셀데이터/아파트분양가격.xlsx")
df_seoul=df[df["지역명"]=="서울"]
result=df_seoul.sort_values(by="분양가격",ascending=True) #ascending: 오름차순
print(result)