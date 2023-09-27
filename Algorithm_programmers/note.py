n,m=map(int,input().split())
queue=[]
for i in range(m):
    paytype,val=input().split()
    val=int(val)
    if paytype=="deposit":
        n+=val
        if queue!=[] and queue[0]<=n:
            n-=queue[0]
            queue.pop(0)
    elif paytype=="pay":
        if n-val>=0:
            n-=val
    elif paytype=="reservation":
        if n>=val:
            n-=val
        else:
            queue.append(val)
    print("잔액 : {} 큐: {}".format(n,queue))
print(n)
        
    
# 0 6
# deposit 10
# pay 5
# reservation 5
# reservation 5
# pay 5
# deposit 10

