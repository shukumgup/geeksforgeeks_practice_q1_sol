n=int(input())
for i in range(n):
    m=int(input())
    arr=[int(x) for x in input().split()]
    if m==1:
        print(1)
        continue
    elif m==2:
        print(-1)
        continue
    tot_sum=sum(arr)
    f_sum=arr[0]
    s_sum=tot_sum-f_sum-arr[1]
    j=1
    flag=0
    while f_sum<=s_sum:
        if f_sum == s_sum:
            print(j+1)
            flag=1
            break
        j=j+1
        f_sum = f_sum + arr[j-1]
        s_sum = s_sum - arr[j]
    if flag==0:
        print(-1)