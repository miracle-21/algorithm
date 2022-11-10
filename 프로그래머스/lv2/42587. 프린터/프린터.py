def solution(priorities, location):
    lst = [(i,l) for l, i in enumerate(priorities)]
    answer = 0

    while lst:
        item = lst.pop(0)
        if lst and max(lst)[0] > item[0]:
            lst.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer