N = int(input())
ans = 0
num = 1
while num < N:
    tmp = num
    for i in str(num):
        tmp += int(i)
    if tmp == N:
        ans = num
        break
    else:
        num += 1
if ans:
    print(ans)
else:
    print(0)