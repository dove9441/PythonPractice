def plus(a,b):
    return a+b

def plusv2(*args):
    result=0
    for i in args:
            result=result+i
    return result
    #파라미터의 개수가 정해져있지 않을 떄.
    #들여쓰기 주의. 함수 영역과 for 영역 구분
def tuplereturn(*args):
        return args
        
    
    
    
    
#print(plus(1,2))
print(plusv2(1,2,3,4,5,6))
x=tuplereturn("x","y","z","a")
for i in x:
    print(i)


