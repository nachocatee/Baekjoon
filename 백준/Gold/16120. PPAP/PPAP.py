s = input()
stack = []
for i in s:
    if len(stack) >= 4:
        stack.append(i)
        if stack[-1] == 'P' and stack[-2] == 'A' and stack[-3] == 'P' and stack[-4] == 'P':
            stack.pop()
            stack.pop()
            stack.pop()
    else:
        stack.append(i)

if ''.join(stack) == 'PPAP':
    print('PPAP')
elif ''.join(stack) == 'P':
    print('PPAP')
else:
    print('NP')