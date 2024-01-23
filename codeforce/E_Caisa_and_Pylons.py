a = int(input())
ls = [int(x) for x in input().split()]
# print(max(ls))
coin = ls[0]
en = 0
for i in range(1,len(ls)):
    en += ls[i-1] - ls[i]
    if en < 0:
        coin+=abs(en)
        en = 0
print(coin)

