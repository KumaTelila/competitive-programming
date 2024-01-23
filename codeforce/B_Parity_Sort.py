
def check_even_or_odd(a, b):
    if a%2 == 0 and b%2 == 0:
        return True
    elif a%2 != 0 and b%2 != 0:
        return True
    return False
t = int(input())
for _ in range(t):
    x = int(input())
    ls = [int(i) for i in input().split()]
    sr = sorted(ls)
    ans = 'YES'
    for i in range(len(sr)):
        if not check_even_or_odd(sr[i], ls[i]):
            ans = 'NO'
            break
    print(ans)
            

