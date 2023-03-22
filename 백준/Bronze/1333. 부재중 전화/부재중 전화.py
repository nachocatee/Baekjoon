N, L, D = map(int, input().split())

album = [0] * ((N * L) + 5 * (N-1))
# print(len(album))
i = 0
cnt = 0
while i < len(album):
    album[i] = 1
    cnt += 1
    if cnt == L:
        i += 6
        cnt = 0
    else:
        i += 1
# print(album)
j = D
while True:
    if j < len(album):
        if album[j] == 0:
            ans = j
            break
        else:
            j += D
    else:
        ans = j
        break

print(ans)