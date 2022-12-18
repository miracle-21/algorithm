def solution(n):
    result = 1
    num = 1
    while result <= n:
        num += 1
        result *= num
    return num-1