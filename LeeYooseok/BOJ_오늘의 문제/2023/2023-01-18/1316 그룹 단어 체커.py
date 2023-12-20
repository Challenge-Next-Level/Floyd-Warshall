from collections import defaultdict
N = int(input())
answer = 0
for _ in range(N):
    text = input()
    alpha_set = defaultdict(int)
    before_alpha = text[0]
    alpha_set[before_alpha] += 1
    for idx in range(1, len(text)):
        if text[idx] != before_alpha:
            alpha_set[text[idx]] += 1
            before_alpha = text[idx]

    if max(alpha_set.values()) <= 1:
        answer += 1

print(answer)