def solution(s, n):
    result = ""
    for i in s:
        if i == ' ':
            result += i
        elif ord(i) <= 90 and ord(i) + n > 90:
            result += chr(ord(i) + n - 26)
        elif ord(i) >= 97 and ord(i) + n > 122:
            result += chr(ord(i) + n - 26)
        else:
            result += chr(ord(i) + n)
    return result