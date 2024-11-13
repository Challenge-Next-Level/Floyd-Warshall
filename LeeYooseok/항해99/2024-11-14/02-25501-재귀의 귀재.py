T = int(input())


def isPalindrome(text, l, r):
    global call_count
    if l >= r:
        return 1
    elif text[l] != text[r]:
        return 0
    else:
        # 함수 호출 횟수 확인
        call_count += 1
        return isPalindrome(text, l + 1, r - 1)


for _ in range(T):
    S = input()
    call_count = 1
    answer = isPalindrome(S, 0, len(S) - 1)
    print(answer, call_count)
