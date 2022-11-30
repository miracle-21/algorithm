from collections import deque

def solution(n):
    q = deque([])
    result = 0
    for i in range(1, n+1):
        q.append(i)
        if sum(q) == n:
            result += 1
            q.popleft()
        while sum(q) > n:
            q.popleft()
            if sum(q) == n:
                result += 1
    return result