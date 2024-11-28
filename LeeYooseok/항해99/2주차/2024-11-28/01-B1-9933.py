from collections import defaultdict

N = int(input())

word_dict = defaultdict(list)

for _ in range(N):
    word = input()
    word_dict[word[0]].append(word)

    reverse_word = word[::-1]

    if reverse_word in word_dict[reverse_word[0]]:
        print(len(reverse_word), reverse_word[len(reverse_word) // 2])
        break
