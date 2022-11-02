def solution(s):
    s = s.split(' ')
    lst = []
    for i in s:
        lst.append(int(i))
    return str(min(lst)) + ' ' + str(max(lst))