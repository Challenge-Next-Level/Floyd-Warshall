import sys

input = sys.stdin.readline

N = int(input())

word_list = list()

for _ in range(N):
    word = input().strip()

    word_list.append(word)

answer_word_list = ["", ""]
max_length = 0

for i in range(N):
    first_word = word_list[i]

    if len(first_word) <= max_length:
        continue

    for j in range(i + 1, N):
        second_word = word_list[j]

        now_length = 0

        min_length = min(len(first_word), len(second_word))

        if min_length <= max_length:
            continue

        for k in range(min_length):
            if first_word[k] == second_word[k]:
                now_length += 1
            else:
                break

        if now_length > max_length:
            max_length = now_length
            answer_word_list = [first_word, second_word]


print(answer_word_list[0])
print(answer_word_list[1])