ls = input().split()
a, k = int(ls[0]), int(ls[1])
ans = []
for i in range(a):
    lsi = input().split()
    f, t = int(lsi[0]), int(lsi[1])
    if t>=k:
        ans.append(f-(t-k))
    else:
        ans.append(f)
print(max(ans))
