import sys
import numpy as np
n=int(input())
data=[]
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
    
day=0
arr=np.array(data)
while True:
    day+=1
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=0:
                print("인덱스 : ",i,j)
                print("데이터" ,arr[i-1:i+1,j-1:j+1])
    break
    
    





# 0 0 1 0
# 2 0 0 0
# 2 2 0 0
# 2 0 0 0