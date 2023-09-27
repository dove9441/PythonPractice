# 0, 1, 1, 2, 3, 5, ...

# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
    
    
  # 파이썬은 일정 이상 재귀하면 런타임 오류가 난단다 코테에서는 시간초과가 나거나.  
n=5
lst = [0,1]
for i in range(2,n+1):
    lst.append(lst[i-1]+lst[i-2])
    
print(lst[len(lst)-1])