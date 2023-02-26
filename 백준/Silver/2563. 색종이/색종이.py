N = int(input())
board = [[0] * 100 for _ in range(100)]
res = 0
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            board[a+i][b+j] += 1
for i in range(100):
    for j in range(100):
        if board[i][j] > 0:
            res += 1
print(res)