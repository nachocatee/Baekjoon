s = input()
N = int(input())
ring_lst = []

for _ in range(N):
    ring = input()
    ring_lst.append(ring)
# print(ring_lst)
cnt = 0
for i in ring_lst:
    for j in range(len(i)):
        if j <= len(i) - len(s):
            if i[j:j+len(s)] == f'{s}':
                cnt += 1
                break
        else:
            if i[j:] + i[:j-(len(i)-len(s))] == f'{s}':
                cnt += 1
                break
print(cnt)