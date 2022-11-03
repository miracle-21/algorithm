def solution(s):
    s = s.lower().split(' ')
    answer = ''
    for i in s[:-1]:
        answer += i.capitalize() + ' '
    return answer + s[-1].capitalize()