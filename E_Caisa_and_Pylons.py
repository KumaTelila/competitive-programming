a, b = map(int, input().split())
ls1 = list(map(int, input().split()))
ls2 = list(map(int, input().split()))
ans = [0]*b
i = 0
j = 0
count = 0
while  j < b:
    if ls1[i] > ls2[j]:
        ans[j] = count
        j+=1
    else:
        i+=1
        count+=1
print(*ans)

    
    


