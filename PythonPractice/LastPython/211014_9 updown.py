import random
ans=random.randint(1,100)
print("Start game")
b=0
count=0
while b!=1:
    n=int(input("choice number >>"))
    count+=1
    if n==ans: 
        print("correct! count={0}".format(count))
        b=1

    elif n>ans:
        print("down")
    else:
        print("up")

