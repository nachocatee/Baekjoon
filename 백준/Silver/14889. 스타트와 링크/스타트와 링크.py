import sys
input = sys.stdin.readline


def backtracking(depth, n):
    global min_
    if depth == N//2:
        team1 = 0
        team2 = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    team1 += board[i][j]
                elif not visited[i] and not visited[j]:
                    team2 += board[i][j]
        min_ = min(min_, abs(team1-team2))
        return
    for i in range(n, N):
        if not visited[i]:
            visited[i] = True
            backtracking(depth+1, i+1)
            visited[i] = False


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
# player = list(range(N))
# for i in board:
#     print(i)
# tmp = []
min_ = 100
backtracking(0, 0)
print(min_)