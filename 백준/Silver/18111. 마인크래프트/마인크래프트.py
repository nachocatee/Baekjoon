import sys

input = sys.stdin.readline
# 세로 N, 가로 M, 인벤토리에 들어있는 블록의 수 B
N, M, B = map(int, input().split())
land = []
min_time = 9876543210
height = 0
for _ in range(N):
    land.append([x for x in map(int, input().split())])
for i in range(257):
    plus_block = 0 # 높게 만들기
    minus_block = 0 # 낮게 만들기
    for x in range(N):
        for y in range(M):
            if land[x][y] > i:
                minus_block += land[x][y] - i
            else:
                plus_block += i - land[x][y]
    if plus_block > B + minus_block:
        continue
    time = minus_block * 2 + plus_block
    if time <= min_time:
        min_time = time
        height = i
print(min_time, height)