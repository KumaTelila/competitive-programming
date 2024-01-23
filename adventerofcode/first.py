def find(a):
    ans = ''
    for i in a:
        if i.isdigit():
            ans+=i
            break
    for i in reversed(a):
        if i.isdigit():
            ans+=i
            break
    return ans

with open('first_input.txt', 'r') as f:
    ls = [find(i.strip()) for i in f.read().split()]
sum = 0
for i in ls:
    sum+=int(i)
print(sum)

