while True:
    n = int(input())
    if n == 0:
        break
    else:
        words = list()
        for _ in range(n):
            word = input()
            words.append(word)
    # print(words)
    words.sort(key= lambda word: word.lower())
    print(words[0])