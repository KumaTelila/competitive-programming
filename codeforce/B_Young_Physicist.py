t = int(input())
a, b, c, = 0, 0, 0
for i in range(t):
    ls = [int(i) for i in input().split()]
    a+=ls[0]
    b +=ls[1]
    c+=ls[2]
if a== 0 and b==0 and c==0:
    print('YES')
else:
    print('NO')
