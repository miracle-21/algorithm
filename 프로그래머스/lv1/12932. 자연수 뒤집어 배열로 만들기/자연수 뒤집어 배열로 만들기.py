def solution(n):
    n = str(n)
    return [int(n[i-1]) for i in range(len(n), 0, -1)]