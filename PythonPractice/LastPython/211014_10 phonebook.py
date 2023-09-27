

nbook=[] #리스트 속 딕셔너리 이용
while True:
    print("1: 전화번호 추가\n2: 전화번호 검색\n3: 전화번호 삭제\n4: 전화번호 전체출력\n5: 종료")
    n=int(input("select menu >> "))
    if n==1:
        name=input("이름 입력 >> ")
        number=input("번호 입력 >> ")
        nbook.append({"name":name, "number":number})
    elif n==2:
        searchname=input("이름 입력 >>")
        for data in nbook:
            find=0
            if data["name"]==searchname :
                find=1
                print("이름: {0} 전화번호: {1}".format(data["name"],data["number"]))
            if find==0:
                print("name not found")
                
             
    elif n==3:
        dname=input("이름 입력 >> ")
        for data in nbook:
            if data["name"]==dname:
                nbook.remove(data)
            else:
                print("not found")
    elif n==4:
        for data in nbook:
            print("이름: {0} 전화번호: {1}".format(data["name"],data["number"]))
    elif n==5:
        print("종료")
        break;
    else:
        print("wrong input")