target = ""
alphabets = ['A', 'E', 'I', 'O', 'U']
answer = 0


def solution(word):
    global target, answer
    target = word
    answer = 0

    for alphabet in alphabets:
        if dfs(alphabet):
            return answer


def dfs(now_string):
    global answer
    answer += 1
    if now_string == target:
        return True

    if len(now_string) == 5:
        return False

    for new_alphabet in alphabets:
        if dfs(now_string + new_alphabet):
            return True


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
