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
    red = []
    green = []
    blue = []
    for j in i:
        ls = j.split()   
        for k in range(1, len(ls)):
            if ls[k] == 'red':
                red.append(int(ls[k-1]))
            if ls[k] == 'green':
                green.append(int(ls[k-1]))
            if ls[k] == 'blue':
                blue.append(int(ls[k-1]))
    sum+=max(red)*max(green)*max(blue)
print(sum)