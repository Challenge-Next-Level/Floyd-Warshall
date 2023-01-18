S = input()

word_set = set()

for l in range(len(S)):
    for i in range(len(S) - l):
        word_set.add(S[i:i + l + 1])

print(len(word_set))
