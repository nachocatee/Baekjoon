N = input()
ans = 0
num = '1'
while int(num) < int(N):
    tmp = int(num)
    for i in num:
        tmp += int(i)
    if tmp == int(N):
        ans = int(num)
        break
    else:
        num = str(int(num) + 1)
if ans:
    print(ans)
else:
    print(0)