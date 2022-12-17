def solution(left, right):
    result = 0
    for i in range(left, right+1):
        lst = []
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                lst.append(j)
                count += 1
        if count % 2 == 0:
            result += max(lst)
        else:
            result -= max(lst)
    return result