def check(lst):
    cnt = 0
    for i in range(4):
        if lst[0][i] != lst[1][i]:
            cnt += 1
        if lst[1][i] != lst[2][i]:
            cnt += 1
        if lst[2][i] != lst[0][i]:
            cnt += 1
    return cnt


def backtracking(n):
    global min_
    if len(tmp) == 3:
        min_ = min(min_, check(tmp))
        return

    for n in range(n, N):
        if not visited[n]:
            visited[n] = 1
            tmp.append(mbti[n])
            backtracking(n+1)
            tmp.pop()
            visited[n] = 0


T = int(input())
for _ in range(T):
    N = int(input())
    mbti = list(map(str, input().split()))
    if N > 32:
        print(0)
    else:
        visited = [0] * N
        tmp = []
        min_ = 9876543210

        backtracking(0)
        print(min_)