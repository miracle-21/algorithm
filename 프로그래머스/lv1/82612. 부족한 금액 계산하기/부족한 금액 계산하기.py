def solution(price, money, count):
    result = 0
    for i in range(count):
        result += price * (i+1)
    if result-money < 0:
        return 0
    return result-money