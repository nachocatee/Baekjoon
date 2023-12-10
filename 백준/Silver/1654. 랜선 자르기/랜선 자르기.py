K, N = map(int, input().split())
length_list = []
for _ in range(K):
    length_list.append(int(input()))
max_len = max(length_list)
min_len = 1
ans_list = []
while min_len <= max_len:
    target = (max_len + min_len) // 2
    nums = 0
    for i in length_list:
        nums += i // target
    if nums >= N:
        ans_list.append(target)
        min_len = target + 1
    else:
        max_len = target - 1
print(max(ans_list))