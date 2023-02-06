N = input()
num = list()
for n in N:
    num.append(n)

num.sort(reverse=True)
# print(num)

result = ''.join(num)
print(result)