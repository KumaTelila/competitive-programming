ls = [int(i) for i in input().split()]
n, m = ls[0], ls[1]
arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
merged = []
i, j = 0, 0
while i< n and j<m:
    if arr1[i] <= arr2[j]:
        merged.append(arr1[i])
        i+=1
    else:
        merged.append(arr2[j])
        j+=1

merged.extend(arr1[i:])
merged.extend(arr2[j:])
print(*merged)
