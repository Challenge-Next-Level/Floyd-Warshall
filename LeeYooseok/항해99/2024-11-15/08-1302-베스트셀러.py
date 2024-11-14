import sys

input = sys.stdin.readline

from collections import defaultdict

N = int(input())

word_dict = defaultdict(int)

for _ in range(N):
    word = input().rstrip()
    word_dict[word] += 1

print(sorted(word_dict, key=lambda x : (-1 * word_dict[x], x))[0])