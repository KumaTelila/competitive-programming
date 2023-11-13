ls = []
for row in range(5):
    row = [int(i) for i in input().split()]
    ls.append(row)
ind = []
for row in range(5):
    for col in range(5):
        if ls[row][col] ==1:
            ind.append(row)
            ind.append(col)
            break
print(abs(ind[0]-2) + abs(ind[1]-2))

