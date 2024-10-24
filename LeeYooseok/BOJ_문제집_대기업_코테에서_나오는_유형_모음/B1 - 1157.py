from collections import defaultdict

word = input().upper()

word_dict = defaultdict(int)

for alphabet in word:
    word_dict[alphabet] += 1

max_cnt = 0
max_word = []
for key, value in word_dict.items():
    if value > max_cnt:
        max_cnt = value
        max_word = [key]
    elif value == max_cnt:
        max_word.append(key)

if len(max_word) >= 2:
    print("?")
else:
    print(max_word[0])