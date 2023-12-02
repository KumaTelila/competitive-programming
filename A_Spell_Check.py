t = int(input())
st ={'T': 1, 'i': 1, 'm': 1, 'u': 1, 'r':1}
for i in range(t):
    n = int(input())
    s = input()
    dic = {}
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i] =1
    ch = "YES"
    
    for i in dic.keys():
        if len(dic) < len(st):
            ch = "NO"
            break
        if i in st and dic[i] != 1:
            ch = "NO"
            break
        elif i not in st:
            ch = 'NO'
            break
    print(ch)
