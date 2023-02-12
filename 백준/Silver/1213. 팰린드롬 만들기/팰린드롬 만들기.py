name = input()
alpa_lst = []
result_lst = [0] * len(name)
for i in name:
    alpa_lst.append(i)
alpa_lst_set = set(alpa_lst)
alpa_lst_set = list(alpa_lst_set)
alpa_lst_set.sort()
alpa_lst.sort()
# print(alpa_lst_set) # ['A', 'B', 'C']
# print(alpa_lst) # ['A', 'A', 'A', 'A', 'B', 'B', 'C]
cnt_lst = []
for i in range(len(alpa_lst_set)):
    cnt_lst.append(alpa_lst.count(f'{alpa_lst_set[i]}'))
# print(cnt_lst) # [4, 2, 1]
for i in range(len(cnt_lst)):
    if cnt_lst[i] % 2: # cnt_lst[i]가 홀수면
        result_lst[len(name) // 2] = alpa_lst_set[i]
        alpa_lst.remove(f'{alpa_lst_set[i]}')
# print(alpa_lst) # ['A', 'A', 'A', 'A', 'B', 'B']

try:
    for i in range(len(name)//2):
        result_lst[i] = result_lst[len(name)-1-i] = alpa_lst[0]
        alpa_lst.remove(f'{alpa_lst[0]}')
        alpa_lst.remove(f'{alpa_lst[0]}')

    for i in result_lst:
        print(''.join(i), end='')
except:
    print("I'm Sorry Hansoo")