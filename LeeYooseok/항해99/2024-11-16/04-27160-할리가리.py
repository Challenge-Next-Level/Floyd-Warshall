import sys

input = sys.stdin.readline

from collections import defaultdict

N = int(input())

card_dict = defaultdict(int)

for _ in range(N):
    S, X = input().rstrip().split()
    card_dict[S] += int(X)

answer = "NO"
for key, value in card_dict.items():
    if value == 5:
        answer = "YES"
        break

print(answer)