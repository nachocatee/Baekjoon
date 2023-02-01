N = int(input())
words = list()
for _ in range(N):
    word = input()
    words.append(word)

words_set = set(words)
words = list(words_set)

words.sort()
words.sort(key= lambda word: len(word))

for i in words:
    print(i)