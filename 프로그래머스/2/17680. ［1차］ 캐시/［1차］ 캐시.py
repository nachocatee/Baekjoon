from collections import deque

def solution(cacheSize, cities):
    q = deque()
    answer = 0
    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for city in cities:
            if city.lower() in q: # q에 이미 있는 도시면
                answer += 1
                q.remove(city.lower())
                q.append(city.lower())
            else:
                if q and len(q) >= cacheSize:
                    q.popleft()
                answer += 5
                q.append(city.lower())
            
    return answer