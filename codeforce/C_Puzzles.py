ls = input().split()
a = int(ls[0])
num = [int(x) for x in input().split()]
num.sort()
_min = float("inf")
i, j = 0, a-1
while j< len(num):
    _min = min(_min, num[j] - num[i])
    i+=1
    j+=1
print(_min)


