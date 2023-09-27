# 자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
# 예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

# n	result
# 78	83
# 15	23


def bigN(n):
    n2 = bin(n)[2:]
    # 1 개수새기
    cnt = 0
    for i in range(0,len(n2)):
        if n2[i] == '1':
            cnt+=1
    
    #다음 큰 숫자 찾기
    nextBig = n
    while(True):
        cntNext = 0 
        nextBig+=1
        nextBig2=bin(nextBig)[2:]
        for i in range(0,len(nextBig2)):
            if nextBig2[i]=='1':
                cntNext+=1
        
        if cntNext ==cnt:
            print("n2 : ",n2 , " 1개수 : ",cnt, " nextBig : ",nextBig, " cnt : ",cnt)
            return nextBig
            
    

print(bigN(78))