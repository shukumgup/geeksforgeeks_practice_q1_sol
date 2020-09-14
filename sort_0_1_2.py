#from collections import defaultdict
n=int(input())
for i in range(n):
    data=[0]*3
    size= int(input())
    arr=[int(x) for x in input().split()]
    arr.sort()
    print(*arr)
