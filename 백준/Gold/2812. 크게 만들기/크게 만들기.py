N, K = map(int, input().split())
num = list(input())

num_list = []
del_num = K

for i in range(N):
    while del_num > 0 and num_list:
        # 제거할 수가 있고 리스트가 있을때까지 반복
        if num_list[len(num_list) - 1] < num[i]:
            # 리스트의 끝 수가 num i번째 수보다 작으면
            num_list.pop()
            del_num -= 1
        else:
            break
    num_list.append(num[i])

# print(num_list) # ['9', '4']

result = ''
for i in range(N - K):
    result += str(num_list[i])

print(result)