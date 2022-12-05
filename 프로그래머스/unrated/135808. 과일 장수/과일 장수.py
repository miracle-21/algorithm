from collections import deque

def solution(k, m, score):
    score.sort(reverse = True)
    q = deque(score)
    result = 0
    while len(q) >= m:
        for _ in range(m-1):
            q.popleft()
        v = q.popleft()
        result += v * m
    return result
        