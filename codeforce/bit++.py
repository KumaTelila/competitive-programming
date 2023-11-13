a = int(input())
sm = 0
for i in range(a):
    print(sm)
    x = input()
    if x == "++X" or x == "X++":
        sm+=1
    else:
        sm-=1
print(sm)
