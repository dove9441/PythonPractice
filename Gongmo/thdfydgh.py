""""
공모전 계획.

1. 데이터 전처리


	


2. 데이터 수집

	공공데이터 활용. 전국주차장좌표.


3. 모델 구성

Regression 모델 사용.

구하려는 Y:
	주차 민원 위험도 ( ex)1~10 )

변수:
	1) 주차장
    
    	데이터 기준 주차장 500M반경의 개수
        
        500이내를 구하는 코드 - 이거 있음
        
        위도 기준으로는 + 0.005이 약 0.5km에 해당하고, 경도 기준으로는 +0.0075가 약 +0.5km 정도
        ㄴ 짜피 의미 없겠네 거리 값이 나오니.
        
        if distance() < 0.5:
        	count+=
        이런식으로 ㄱ
        
        여기서 드는 의문점 하나.
        하나의 데이터 기준으로 모든 주차장 위도, 경도 값을 계산하는건 비효율적이지 않나?
        	ㄴ근처 데이터 값으로미리 짤라놔야하지 않을까? 
            어떤 걸 자른다는 거 -> 주차장 데이터. 이게 전국이잖. 하나의 데이터의 주차장 개수를 구하자고 전국 데이터의 거리를 계산할 필요가 없다.
            	이러면 만오천(주차장개수)X 이십만(데이터개수) ㅋㅋ; 30억? ㄱㅊ?
            뭐 나중에 고민할 문제인가.거
            그렇긴 하네
            
            해결할 답이 생각이 안 나는데
    		ㅅㅂ 나도 안떠오름
            
            그냥 계산 떄려봄 시간 되나
            
    2) 시간
    	이건 일단 보류

"""

"""
이제 뭐하지?




"""

