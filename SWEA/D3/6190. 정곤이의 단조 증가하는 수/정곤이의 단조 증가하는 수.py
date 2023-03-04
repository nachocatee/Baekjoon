t = int(input())

def danjo(n):
    n = str(n)
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return 0
    return 1

for tc in range(1,t+1):
    n = int(input())
    a = list(map(int,input().split()))
    maxn = 0
    for i in range(n-1):
        for j in range(i+1,n):
            num = a[i]*a[j]
            if danjo(num):
                maxn = max(num,maxn)
        if maxn == 0:
            maxn = -1

    print('#%d %d' % (tc,maxn))