def solution(a, b, n):
    result = 0
    while n//a != 0:
        result += (n//a)*b
        n = (n//a)*b + (n%a)        
    return result