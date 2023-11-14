a = input()
luck = [i for i in a if i =='4' or i =='7']
if len(luck) == len(a):
    print("YES")
else:
    print("NO")
