N, K = map(int, input().split())
coin_list = []
count = 0
for _ in range(N):
    coins = int(input())
    coin_list.append(coins)
# print(coin_list) # [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
coin_list.sort(reverse=True)
# print(coin_list) # [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
for i in coin_list:
    count += K // i
    K = K % i
print(count)