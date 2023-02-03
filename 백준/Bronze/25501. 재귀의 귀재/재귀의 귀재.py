def recursion(s, l, r):
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


def is_recursion(s, l, r):
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return is_recursion(s, l+1, r-1) + 1

def is_isPalindrome(s):
    return is_recursion(s, 0, len(s)-1) + 1


T = int(input())
S_list = list()
count = 0
for t in range(1, T+1):
    S = input()
    if isPalindrome(S) == 1:
        print(isPalindrome(S), is_isPalindrome(S) - 1)
    else:
        print(isPalindrome(S), is_isPalindrome(S))