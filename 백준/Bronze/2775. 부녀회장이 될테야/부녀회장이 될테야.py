T = int(input())
for _ in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    house = [x for x in range(1, n+1)] # 0층
    for i in range(k):
        for j in range(1, n):
            house[j] += house[j-1]
    print(house[-1])