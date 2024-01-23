a = [int(i) for i in input().split()]
l = a[0]
r = a[1]
x = a[2]
y = a[3]
k = a[4]
f = False
for i in range(x, y+1):
    _a = k*i
    if l<= _a <=r:
        f = True
if f:
    print("YES")
else:
    print("NO")

        

