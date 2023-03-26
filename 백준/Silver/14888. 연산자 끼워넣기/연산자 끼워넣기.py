def backtracking(n, ans, a, b, c, d):
    global max_
    global min_
    if n == N:
        max_ = max(max_, ans)
        min_ = min(min_, ans)
        return

    if a:
        backtracking(n + 1, ans + A[n], a - 1, b, c, d)
    if b:
        backtracking(n + 1, ans - A[n], a, b - 1, c, d)
    if c:
        backtracking(n + 1, ans * A[n], a, b, c - 1, d)
    if d:
        backtracking(n + 1, int(ans / A[n]), a, b, c, d - 1)


N = int(input())
A = list(map(int, input().split()))
plus, minus, multi, divide = map(int, input().split()) # 덧셈 뺄셈 곱셈 나눗셈

max_ = -9876543210
min_ = 9876543210

backtracking(1, A[0], plus, minus, multi, divide)
print(max_)
print(min_)