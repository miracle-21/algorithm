from collections import deque

def solution(storey):
    storey = list(map(int, str(storey)))
    q = deque([i for i in reversed(storey)])
    q.append(0)
    result = 0
    while q:
        num = q.popleft()
        if num > 5 or num == 5 and q[0] >=5:
            result += 10-num
            q[0] += 1
        else:
            result += num
    return result