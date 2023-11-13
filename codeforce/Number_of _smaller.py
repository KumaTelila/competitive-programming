ls = [int(i) for i in input().split()]
n, m = ls[0], ls[1]
arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
first = 0
ans = []
for i in arr2:
    while first< len(arr1) and i > arr1[first]:
        first += 1
    ans.append(first)
print(*ans)
    
