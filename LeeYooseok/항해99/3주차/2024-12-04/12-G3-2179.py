import sys

input = sys.stdin.readline

N = int(input())
word_list = [list(input().rstrip()) for _ in range(N)]

answer = ["", ""]
answer_value = 0

for i in range(N):
    word_1 = word_list[i]

    if len(word_1) <= answer_value:
        continue
    for j in range(i + 1, N):
        word_2 = word_list[j]

        if len(word_2) <= answer_value:
            continue

        if word_1[:answer_value + 1] != word_2[:answer_value + 1]:
            continue

        for k in range(answer_value, min(len(word_1), len(word_2))):
            if word_1[k] != word_2[k]:
                break

            answer = [word_1, word_2]
            answer_value += 1

print("\n".join(["".join(w) for w in answer]))


