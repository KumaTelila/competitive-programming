from collections import Counter
def solution(s, k):
    i = 0
    j = k-1
    count = 0
    sub = Counter(s[i:j+1])
    while j< len(s):
        if len(sub) == k:
            count+=1
        j+=1
        if j == len(s):
            break
        sub[s[i]]-=1
        sub[s[j]]+=1
        
        if sub[s[i]] == 0:
            del sub[s[i]]
        i+=1
        
    return count
s = "homed"
k = 5
print(solution(s, k))