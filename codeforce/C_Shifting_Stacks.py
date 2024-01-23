t = int(input())
for _ in range(t):
    n = int(input())
    ls = [int(i) for i in input().split()]
    flag = True
    stack = []
    stack.append(ls[0])
    for i in range(1, n):
        top = stack[-1]
        if top > ls[i] and top-1 == ls[i]:
            flag = True
        elif top < ls[i] and top+1 ==ls[i]:
            flag = True
        elif top == ls[i]:
            flag = True
        else:
            flag = False
        stack.pop()
        stack.append(ls[i])
    if flag:
        print('YES')
    else:
        print('NO')




