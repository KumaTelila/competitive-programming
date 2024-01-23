def select(ls1, ls2):
    new = []
    i = 0
    n = len(ls1)
    m = len(ls2)
    if n%2 == 0:
        new.extend(ls2[:n//2])
        new.extend(ls2[::-1][:n//2])
    else:
        new.extend(ls2[:n//2+1])
        new.extend(ls2[::-1][:n//2+1])
    return new
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ls1 = list(map(int, input().split()))
    ls2 = list(map(int, input().split()))
    ls1.sort()
    ls2.sort()
    new = select(ls1, ls2)
    new.sort(reverse=True)
    ans = 0
    if n%2 ==0:
        for i in range(n):
            ans+=abs(ls1[i] - new[i])
    else:
        mid  = n//2
        if abs(ls1[mid] - new[mid]) > abs(ls1[mid] - new[mid+1]):
            del new[mid+1]
        else:
            del new[mid]
        for i in range(n):
            ans+=abs(ls1[i] - new[i])
    print(ans)
