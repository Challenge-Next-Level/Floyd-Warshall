def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        prev, now = phone_book[i], phone_book[i + 1]

        if len(prev) <= len(now):
            if prev == now[:len(prev)]:
                return False

    return True