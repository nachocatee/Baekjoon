isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
code = '(' + input() + ')'
stack = []
result = []
for i in code:
    if i.isalpha():
        result.append(i)
    elif i == '(':
        stack.append(i)
    elif i in '+-*/':
        if isp[stack[-1]] < isp[i]:
            stack.append(i)
        else:
            while isp[stack[-1]] >= isp[i]:
                a = stack.pop()
                result.append(a)
            stack.append(i)
    else: # 닫는 괄호일 때
        while stack[-1] != '(': # 여는 괄호일때까지
            a = stack.pop()
            result.append(a)
        stack.pop() # 여는 괄호 삭제

print(*result, sep='')