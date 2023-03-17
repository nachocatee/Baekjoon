board = [[0] * 1001 for _ in range(1001)]
N = int(input()) # 색종이의 장수
max_x = 0
max_y = 0
for n in range(1, N+1):
    x1, y1, x2, y2 = map(int, input().split())
    max_x = max(max_x, x1+x2)
    max_y = max(max_y, y1+y2)
    for i in range(x1, x1+x2):
        for j in range(y1, y1+y2):
            board[i][j] = n

for n in range(1, N+1):
    cnt = 0
    for i in range(max_x+5):
        for j in range(max_y+5):
            if board[i][j] == n:
                cnt += 1
    print(cnt)