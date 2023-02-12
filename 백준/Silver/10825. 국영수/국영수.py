N = int(input())
scores = []
for _ in range(N):
    score = list(input().split())
    scores.append(score)

scores.sort(key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(N):
    print(scores[i][0])