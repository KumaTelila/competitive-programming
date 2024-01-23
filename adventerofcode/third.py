def solution(a):
    ind = 1
    _sum = 0
    for ele in a:
        red = 0
        blue = 0
        green = 0
        for j in range(len(ele)):
            if ele[j] == 'red':
                red+=int(ele[j-1])
            if ele[j] == 'green':
                green+=int(ele[j-1])
            if ele[j] == 'blue':
                blue+=int(ele[j-1])
        if red <= 12 and green <=13 and blue <=14:
            _sum+=ind
        ind+=1 
    return _sum
with open('first_input.txt', 'r') as f:
    a = f.read()
count = 1
word = []
for ele in a.split('\n'):
    ele = ele.replace(',', '')
    word.append(ele[7:].split(';'))
sum = 0 
for i in word:
    flag = True
    for j in i:
        ls = j.split()
        for k in range(1, len(ls)):
            if ls[k] == 'red' and int(ls[k-1])>12:
                print(ls[k], ls[k-1])
                flag = False
                break
            if ls[k] == 'green' and int(ls[k-1])>13:
                print(ls[k], ls[k-1])
                flag = False
                break
            if ls[k] == 'blue' and int(ls[k-1])>14:
                print(ls[k], ls[k-1])
                flag = False
                break
    if flag:
        sum+=count
    count+=1
print(sum)

