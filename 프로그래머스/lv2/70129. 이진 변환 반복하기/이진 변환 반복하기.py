def solution(s):
    zero = 0
    count = 0
    while s != '1':
        zero += s.count('0')
        s = format(s.count('1'), 'b')
        count += 1
    return [count, zero]