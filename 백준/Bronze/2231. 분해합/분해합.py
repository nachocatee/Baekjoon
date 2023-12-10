N = input()
res_list = []
num = '1'
while int(num) < int(N):
    tmp = int(num)
    for i in num:
        tmp += int(i)
    if tmp == int(N):
        res_list.append(int(num))
        break
    else:
        num = str(int(num) + 1)
if res_list:
    print(min(res_list))
else:
    print(0)