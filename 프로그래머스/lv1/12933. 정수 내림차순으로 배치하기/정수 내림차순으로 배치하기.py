def solution(n):
    n = sorted(list(map(str, str(n))), reverse=True)
    answer = ''
    for i in n:
        answer += i
    return int(answer)