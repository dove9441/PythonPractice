fruit={"사과":100, "포도":200, "토마토":329}
print(fruit)
print(fruit["사과"])
fruit["오렌지"]=999 # 원소 추가
del fruit["사과"] #원소 삭제
fruit.pop("토마토") #원소 삭제
print(fruit)
fruit["포도"]=300 #원소 수정