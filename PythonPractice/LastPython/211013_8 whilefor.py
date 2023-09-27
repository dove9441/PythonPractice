num=1
while num!=100 :
    print(num)
    num+=1

for i in [1,2,3,4,5,6]: #튜플이나 리스트 자료형 또는 range 함수가 온다.
    print(i)  # 탭키 들여쓰기가 필수이다. 들여쓰기 하지 않으면 동작하지 않는다.

for j in ["일","이","삼"]:
    print(j)

n=0
for k in range(50,100): #50~99까지 50번 반복한다. 50(1번)부터 시작
    n=n+1
    print("{0}번째 출력입니다. hello, world!".format(n))

    # range 함수: 매개변수 1개: 0부터 A-1까지의 숫자 반환/ 2개: A부터 B-1까지의 숫자 반환 
    # 3개: A부터 B-1까지, C간격으로 B-1까지 숫자 반환