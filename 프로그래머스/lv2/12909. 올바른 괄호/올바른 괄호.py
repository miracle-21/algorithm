def solution(s):
    x = 0
    for i in s:
        if x < 0:
            break
        if i =="(":
            x += 1
        elif i ==")":
            x -= 1
    return x == 0

    # 효율성테스트2 실패
    # if s.count("(") == s.count(")"):
    #     while "()" in s:
    #         s = s.replace("()","")
    #     return s == ""
    # else:
    #     return False