N = int(input())
target_word = list(input())
word_list = [input() for _ in range(N - 1)]

answer = 0
for word in word_list:
    target = target_word[:]

    diff_cnt = 0

    for w in word:
        if w in target:
            target.remove(w)
        else:
            diff_cnt += 1

    # 서로 다른 문자가 2개 미만이고, target 의 남아있는 길이도 2개 미만일때
    if diff_cnt < 2 and len(target) < 2:
        answer += 1

print(answer)