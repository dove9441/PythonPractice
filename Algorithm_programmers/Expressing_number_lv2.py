n = 15



# 1~n까지의 합은 s=n*(n+1)/2. k+1부터 n까지의 합은 n*(n+1)/2 - k*(k-1)/2이다.

def sum(n):
    return n*(n+1)/2

def sumkn(k,n):
    return (n*(n+1)/2) - (k*(k+1)/2)


def solution(n):
    cnt = 0
    for i in range(0,n):
        for j in range(i,n):
                if sumkn(i,j) == n:
                    cnt+=1
                elif sumkn(i,j)>n:
                    continue
    
    
    
    return cnt+1;

print(sumkn(0,5))
print(solution(n))