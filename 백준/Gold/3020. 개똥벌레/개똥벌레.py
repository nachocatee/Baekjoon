N, H = map(int, input().split())
bottom = [0] * (H + 1)
top = [0] * (H + 1)

for i in range(N):
    if i % 2:
        top[int(input())] += 1
    else:
        bottom[int(input())] += 1

for i in range(H - 1, 0, -1):
    bottom[i] += bottom[i + 1]
    top[i] += top[i + 1]

min_ = N
cnt = 0
for i in range(1, H + 1):
    min_ = min(min_, bottom[i] + top[H - i + 1])

for i in range(1, H + 1):
    if bottom[i] + top[H - i + 1] == min_:
        cnt += 1

print(min_, cnt)