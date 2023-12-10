import sys

input = sys.stdin.readline
n = int(input())
stack = []
lst = []
res = []
tmp = 1
for i in range(1, n+1):
    num = int(input())
    if num < tmp:
        if stack and stack[len(stack)-1] == num:
            lst.append(stack.pop())
            res.append('-')
        continue
    else:
        while num > tmp:
            stack.append(tmp)
            res.append('+')
            tmp += 1
        else:
            lst.append(tmp)
            tmp += 1
            res.append('+')
            res.append('-')
if stack:
    print('NO')
else:
    for i in res:
        print(i)