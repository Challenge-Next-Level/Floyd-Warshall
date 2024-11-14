S = input()
len_S = len(S)

word_set = set()
for i in range(1, len_S + 1):
    for j in range(len_S - i + 1):
        word_set.add(S[j:j + i])

print(len(word_set))