L = int(input()) # 문자열의 길이
words = input() # 문자열
ans = 0
for i in range(L):
    ans += (ord(words[i]) - 96) * (31 ** i)
print(ans % 1234567891)