sum_score_list = []

for n in range(1, 6):
    score = map(int, input().split())
    sum_score_list.append(sum(score))

# print(sum_score_list)

max_score = max(sum_score_list)
# print(max_score)

for i in range(5):
    if sum_score_list[i] == max_score:
        print(f'{i+1} {max_score}')