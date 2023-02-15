dx = [0, 0, -1, 1] # 좌 우 상 하
dy = [-1, 1, 0, 0]

T = int(input())
for t in range(1, T+1):
    M, N, K = map(int, input().split()) # 가로, 서로, 배추개수
    board = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split()) # 배추 위치
        board[Y][X] = 1

    visited = [[False] * M for _ in range(N)]
    stack = []
    cnt = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and not visited[i][j]:
                stack.append((i, j))
                visited[i][j] = True
                cnt += 1

                while stack:
                    x, y = stack.pop()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                            if board[nx][ny] == 1:
                                stack.append((nx, ny))
                                visited[nx][ny] = True


    print(cnt)