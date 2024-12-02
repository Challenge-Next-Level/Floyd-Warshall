import sys

input = sys.stdin.readline

N = int(input())
word_set = set()
for _ in range(N):
    word_set.add(input().rstrip())

print("\n".join(sorted(list(word_set), key=lambda x: (len(x), x))))
