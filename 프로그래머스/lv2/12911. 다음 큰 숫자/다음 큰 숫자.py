def solution(n):
    count = format(n, 'b').count('1')
    n += 1
    while count != format(n, 'b').count('1'):
        n += 1
    return n