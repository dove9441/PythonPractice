alphabet=["a","b","c","d","e"] #c언어와 같이 인덱스는 0부터 시작
print(alphabet)
alphabet.append("f")  # 마지막 위치에 추가
print(alphabet)
alphabet.remove("f") # 원소 삭제
del alphabet[4] #인덱스 번호의 원소 삭제
print(alphabet)
alphabet[0]="K" #원소 수정
print(alphabet)