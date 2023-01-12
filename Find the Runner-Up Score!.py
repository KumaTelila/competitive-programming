if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ls = []
    for i in arr:
        if(i in ls):
            continue
        ls.append(i)
    ls.sort()
    print(ls[-2])
    
    