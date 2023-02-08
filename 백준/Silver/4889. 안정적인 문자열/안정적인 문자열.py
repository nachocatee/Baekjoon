res_list = []
while True:
    char = input()
    if '-' in char:
        break
    lst = []
    cnt = 0
    res = 0
    for i in range(len(char)):
        if char[i] == '{': # 열리는 괄호라면
            lst.append('{')
        elif char[i] == '}' and len(lst) > 0: # 닫히는 괄호이고 {가 리스트에 있다면
            lst.pop()
        elif char[i] == '}' and len(lst) == 0:
            cnt += 1
            lst.append('}')
    # print(cnt)
    # print(lst)
    res = cnt + len(lst)//2
    # print(res)
    res_list.append(res)
for i in range(len(res_list)):
    print(f'{i+1}. {res_list[i]}')