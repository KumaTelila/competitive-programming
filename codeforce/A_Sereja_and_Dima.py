x = int(input())
arr1 = [int(i) for i in input().split()]
i, j = 0, len(arr1) -1
ser = 0
dim = 0
k = 0
while i <=j:
    if k%2 ==0:
        if arr1[i] > arr1[j]:
            ser+=arr1[i]
            i+=1
        else:
            ser+=arr1[j]
            j-=1
    else:
        if arr1[i] > arr1[j]:
            dim+=arr1[i]
            i+=1
        else:
            dim+=arr1[j]
            j-=1
    k+=1
print(ser, dim)