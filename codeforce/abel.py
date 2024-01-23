"""
arr = [[1, 2, ]]
"""
from collections import Counter
def sol(arr):
    ls= []
    for i in arr:
        ls.extend(i)
    count = Counter(ls)
    print(count)
    for i in arr[0]:
        if count[i] == len(arr):
            return i
    return -1
arr = [[1, 2, 3], [2, 3, 4], [2,3, 10], [2,4, 10 ]]
print(sol(arr))
