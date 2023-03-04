T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    num_lst = []
    for i in range(N-1):
        for j in range(i, N):
            if i != j:
                num_lst.append(arr[i] * arr[j])
    res = [-1]
    for i in num_lst:
        a = i
        tmp = []
        cnt = 0
        while a > 0:
            tmp.append(a % 10)
            a //= 10
        # print(tmp)
        for j in range(len(tmp)-1):
            if tmp[j] >= tmp[j+1]:
                cnt += 1
        if cnt == len(tmp)-1:
            res.append(i)
    print(f'#{t} {max(res)}')