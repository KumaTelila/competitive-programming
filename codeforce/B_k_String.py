from collections import Counter
k = int(input())
s = input()


def check(s, k):
    count = Counter(s)
    for i, j in count.items():
        if j%k != 0:
            return -1
    ans = ''
    for i, j in count.items():
        x = i*(j//k)
        ans += x
    return ans*k
print(check(s, k))