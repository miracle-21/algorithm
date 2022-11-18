def solution(sizes):
    x,y = 0, 0
    for i in sizes:
        x,y = max(max(i), x), max(min(i), y)
    return x*y