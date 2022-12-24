def solution(X, Y):
    result = ''
    for i in range(9,-1,-1):
        result += str(i)*min(X.count(str(i)), Y.count(str(i)))
    if result == '':
        return "-1"
    elif len(result) == result.count("0"):
        return "0"
    else:
        return result