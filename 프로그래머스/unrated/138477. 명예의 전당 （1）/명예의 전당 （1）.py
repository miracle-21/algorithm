from collections import deque

def solution(k, score):
    answer = []
    result = []
    q = deque(score)
    while q:
        answer.append(q.popleft())
        if len(answer) > k:
            answer.remove(min(answer))
        result.append(min(answer))
    return result