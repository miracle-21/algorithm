def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        if phone_book[i-1] != phone_book[i][0:len(phone_book[i-1])]:
            continue
        elif phone_book[i-1] in phone_book[i]:
            return False
    return True
