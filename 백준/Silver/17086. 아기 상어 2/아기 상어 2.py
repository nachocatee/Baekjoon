dx = [-1, 1, 0, 0, -1, -1, 1, 1] # 상 하 좌 우 좌상 우상 좌하 우하
dy = [0, 0, -1, 1, -1, 1, -1, 1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
# for i in board:
#     print(i)

q = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1


while q:
    x, y = q.pop(0)
    for d in range(8):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

# for i in visited:
#     print(i)

max_ = 0
for i in range(N):
    for j in range(M):
        max_ = max(max_, visited[i][j])

print(max_ - 1)