words = ["hello", "one", "even", "never", "now", "world", "draw"]
n = 2

def solution(n, words):
    lst = []
    for i in range(0,len(words)-1): 
        lst.append(words[i])
        if words[i][-1] != words[i+1][0] or words[i+1] in lst:
            return [1,int((i+1)/n+1)] if (i+1)%n==0 else [(i+1)%n+1,int((i+1)/n+1)]

    return [0,0]
print(solution(n,words))