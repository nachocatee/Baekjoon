N = int(input())
lst = []
for _ in range(N):
    title = input()
    lst.append(title)
# print(lst.count(lst[0]))
lst.sort()
cnt_list = []
for i in lst:
    cnt_list.append(lst.count(i))
# print(cnt_list)
print(lst[cnt_list.index(max(cnt_list))])