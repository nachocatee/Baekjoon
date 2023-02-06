N = int(input())
num_list = []
for _ in range(N):
    numbers = int(input())
    num_list.append(numbers)
num_list.sort()
for i in num_list:
    print(i)