A = list(map(int, input()))
B = list(map(int, input()))
res = [0] * 16
for i in range(16):
    if i % 2: # 홀수면
        res[i] = B[i//2]
    else:
        res[i] = A[i//2]

while len(res) > 2:
    tmp = []
    for i in range(len(res)-1):
        num = (res[i] + res[i+1]) % 10
        tmp.append(num)
    res = tmp
print(*res, sep='')