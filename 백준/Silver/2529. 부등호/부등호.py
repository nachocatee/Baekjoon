def check(i, j, k):
    if k == '<':
        return i < j
    else:
        return i > j


def backtracking(n, ans):
    global min_, max_
    if n == k+1:
        max_ = max(max_, int(ans))
        min_ = min(min_, int(ans))
        return

    for i in range(10):
        if not visited[i]:
            if n == 0 or check(ans[-1], str(i), kiho[n-1]):
                visited[i] = 1
                backtracking(n+1, ans+str(i))
                visited[i] = 0


k = int(input())
kiho = input().split()
visited = [0] * 10
max_ = 0
min_ = 9876543210
backtracking(0, '')
print(max_)
if len(str(min_)) == k+1:
    print(min_)
else:
    print(f'0{min_}')