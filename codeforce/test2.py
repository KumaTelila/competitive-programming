from collections import Counter
def generate(s):
    ls = [i for i in s]
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                ls.append(s[i:j+1])
    print(len(ls))
    return ls
def sol(s):
    ans = 0
    dic = Counter(s)
    print(dic)
    for i, j in dic.items():
        ans+=j*(j+1)//2
    return ans
s = 'abcbaccc'
# print(sol(s))
print(sorted(generate(s)))