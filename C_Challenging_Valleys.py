t = int(input())
for _ in range(t):
    n = int(input())
    ls = [int(i) for i in input().split()]
    mn = min(ls)
    b = 0
    for i in range(1, n):
        if ls[i] <= ls[i-1] and b ==0:
            continue
        else:
            b =1
        if ls[i]>=ls[i-1] and b == 1:
            continue
        else:
            b=-1
    if n == 1:
        print("NO")
    elif b == 0 or b == 1:
        print("YES")
    else:
        print("NO")
    
    
    
