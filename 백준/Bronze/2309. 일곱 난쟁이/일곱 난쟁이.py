def backtracking(n):
    global flag
    if len(lst) == 7:
        if sum(lst) == 100 and not flag:
            lst.sort()
            print(*lst, sep='\n')
            flag = 1
    for n in range(n, 9):
        if not visited[n]:
            visited[n] = True
            lst.append(height[n])
            backtracking(n+1)
            lst.pop()
            visited[n] = False

flag = 0
height = []
lst = []
for _ in range(9):
    a = int(input())
    height.append(a)
visited = [False] * (max(height) + 1)
backtracking(0)