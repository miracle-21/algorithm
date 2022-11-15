def solution(phone_book):
    phone_book.sort()
    dict = {}
    for i in phone_book:
        try:
            dict[i[0]] += 1
            return False
        except:
            dict[i[0]] = 0
    return True