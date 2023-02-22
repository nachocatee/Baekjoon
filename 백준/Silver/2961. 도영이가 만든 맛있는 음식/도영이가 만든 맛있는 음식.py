N = int(input()) # 재료의 개수
flavor = [list(map(int, input().split())) for _ in range(N)]
# print(flavor) # [[1, 7], [2, 6], [3, 8], [4, 9]]
res = []
for i in range(1, 1<<N): # 부분집합 만들기
    sour = 1 # 곱 초기값
    bitter = 0 # 합 초기값
    for j in range(N):
        if i & (1<<j):
            sour *= flavor[j][0]
            bitter += flavor[j][1]
    res.append(abs(sour - bitter))
print(min(res))