def solution(x, y, n):
    answer = 0 # 횟수
    res = set()
    res.add(x)
    while res:
        if y in res:
            return answer
        tmp = set()
        for i in res:
            if i + n <= y:
                tmp.add(i + n)
            if i * 2 <= y:
                tmp.add(i * 2)
            if i * 3 <= y:
                tmp.add(i * 3)
        res = tmp
        answer += 1
    return -1