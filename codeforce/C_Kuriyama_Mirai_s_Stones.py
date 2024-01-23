a = int(input())
v = [int(i) for i in input().split()]
sr = sorted(v)
m = int(input())
for i in range(m):
    e,f,g = input().split()
    l = int(f)- 1
    r =int(g)
    sm = 0 
    if int(e) == 1:
        for j in range(l, r):
            sm+=v[j]
    else:
        for j in range(l, r):
            sm+=sr[j]
    print(sm)