dx = [0, 0, 1, -1, 1, 1, -1, -1] # 왼 오 아래 위 왼아래 오아래 왼위 오위
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

while True:
    w, h = map(int, input().split()) # w 지도의 너비, h 높이
    if w == 0 and h == 0:
        break
    land = [list(map(int, input().split())) for _ in range(h)] # 1은 땅, 0은 바다
    visited = [[False] * w for _ in range(h)]
    stack = []
    cnt = 0
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1 and not visited[i][j]:
                stack.append((i, j))
                visited[i][j] = True
                cnt += 1

                while stack:
                    x, y = stack.pop()
                    for d in range(8):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                            if land[nx][ny] == 1:
                                stack.append((nx, ny))
                                visited[nx][ny] = True
    print(cnt)