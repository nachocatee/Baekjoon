N = int(input())
result = 0
for _ in range(N):
    words = input()
    new_words = ''
    count = 0
    for i in range(len(words)-1):
        if words[i] != words[i+1]: # 다음 문자열이 다르면
            new_words = words[i+1:] # words[i] 탈락
            if new_words.count(words[i]) > 0: # 만약 남은 문자열에서 words[i]가 있다면
                count += 1
    # print(count)
    if count == 0: # 그룹단어면
        result += 1
print(result)