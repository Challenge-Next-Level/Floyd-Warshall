from itertools import permutations

n = int(input())

words = list()

for _ in range(n):
    text = list(input())
    text.sort()
    text = ''.join(text)

    if text not in words:
        words.append(text)

for w in words:
    for r in list(permutations(list(w), len(w))):
        print(''.join(r))