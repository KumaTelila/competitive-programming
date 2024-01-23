import re
from collections import OrderedDict
def digit_to_str(a):
    digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    num = ['one', 'two', 'three','four','five','six','seven','eight','nine']
    dic = {'one': '1', 'two': '2', 'three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8', 'nine': '9'}
    dic2 = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    first = {}
    last = {}
    for i in num:
        match = re.search(i, a)
        match2 = a.rfind(i)
        if match:
            last[i] = match2
            if i in first:
                continue
            else:
                first[i] = match.start()
    for i in digit:
        match = re.search(i, a)
        match2 = a.rfind(i)
        if match:
            elem = dic2[i]
            if elem in first:
                first[elem] = min(first[elem], match.start())
            else:
                first[elem] = match.start()
            if elem in last:
                last[elem] = max(last[elem], match2)
            else:
                last[elem] = match2
    first = dict(sorted(first.items(), key=lambda item: item[1]))
    last = dict(sorted(last.items(), key=lambda item: item[1]))
    first_key = next(iter(first))
    last_key = next(reversed(last))
    return dic[first_key]+dic[last_key]
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


print(re.search('three', 'threethreekv33eightninethree'))
with open('first_input.txt', 'r') as f:
    ls = [digit_to_str(i) for i in f.read().split()]
sum = 0
print(ls)
for i in ls:
    sum+=int(i)
print(sum)