N = int(input())
ramen = list(map(int, input().split()))
cost = 0
i = 0

for i in range(N-2):
    if ramen[i] and ramen[i+1] and ramen[i+2]:
        if ramen[i+1] > ramen[i+2]:
            a = min(ramen[i], ramen[i+1] - ramen[i+2])
            cost += 5 * a
            ramen[i] -= a
            ramen[i+1] -= a

            a = min(ramen[i], ramen[i + 1], ramen[i + 2])
            cost += 7 * a
            ramen[i] -= a
            ramen[i + 1] -= a
            ramen[i + 2] -= a
        else:
            a = min(ramen[i], ramen[i+1], ramen[i+2])
            cost += 7 * a
            ramen[i] -= a
            ramen[i+1] -= a
            ramen[i+2] -= a

for i in range(N-1):
    if ramen[i] and ramen[i+1]:
        a = min(ramen[i], ramen[i+1])
        cost += 5 * a
        ramen[i] -= a
        ramen[i+1] -= a
for i in range(N):
    if ramen[i]:
        cost += ramen[i] * 3
print(cost)