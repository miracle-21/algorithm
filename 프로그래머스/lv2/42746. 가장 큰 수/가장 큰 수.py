def solution(numbers):
    lst = []
    answer = ''
    for i in numbers:
        lst.append(str(i))
    lst.sort(key = lambda x : x*3, reverse=True)
    for i in lst:
        answer += i
    return str(int(answer))