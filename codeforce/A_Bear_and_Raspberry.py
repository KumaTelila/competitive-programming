ls = input().split()
a = int(ls[1])
num = [int(x) for x in input().split()]
ans = 0
for i in range(1, len(num)):
    if num[i] < num[i-1]:
        ans = max(ans, num[i-1] - num[i] - a)
print(ans)
