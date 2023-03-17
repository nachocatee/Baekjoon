n = 1003001
a = [False, False] + [True]*(n-1)
primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

N = int(input())
for i in primes:
    if N <= i and str(i) == str(i)[::-1]:
        print(i)
        break