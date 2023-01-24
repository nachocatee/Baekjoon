num = int(input())
result = []
for i in range(num + 1):
    result.append(2 ** i)
    i += 1

print(*result)