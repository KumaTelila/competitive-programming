n = int(input())
if n == 2 or n == 6:
    print("YES")
else:
    if (n/2)%2 == 0:
        print("YES")
    else:
        print("NO")