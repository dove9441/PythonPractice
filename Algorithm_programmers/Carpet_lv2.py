def solution(brown, yellow):
    n=3
    m=3
    for m in range(3,2005000):
        for n in range(3,2005000):
            if 2*(n+m)==(brown+4) and n*m==brown+yellow:
                lst = [n,m]
                return lst
            elif n*m>brown+yellow:
                break;
                

    