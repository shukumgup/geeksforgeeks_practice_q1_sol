# code
n = int(input())
data = []
for i in range(n):
    o, p = map(int, input().split())
    ts = 0
    arr = [int(x) for x in input().split()]
    j = 0
    k = 0
    rs = p
    flag = 0
    while True:
        flag = 0
        while True:

            if ts == p:
                flag = 1
                break
            elif ts > p:
                flag = 2
                break
            else:
                try:
                    ts = ts + arr[j]
                    j = j + 1
                    #print(ts, j, k)
                    if j==o:
                        flag=3
                        break
                except:
                    flag=2
                    break
        #print(flag)
        if flag == 1:
            print(k+1, j)
            break
        elif flag == 2:
            ts=ts-arr[k]
            k=k+1
        elif flag==3:
            if ts<p:
                print(-1)
                break
        if k==o:
            print(-1)
            break


