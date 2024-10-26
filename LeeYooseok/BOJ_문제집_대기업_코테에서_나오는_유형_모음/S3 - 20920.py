import sys
from collections import defaultdict

# 길이가 M이상인 단어들만 외움
# 자주 나오는 단어일수록 앞에 배치한다.
# 해당 단어의 길이가 길수록 앞에 배치한다.
# 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
input = sys.stdin.readline

N, M = map(int, input().split())

word_dict = defaultdict(int)
for _ in range(N):
    word = input().rstrip()
    if len(word) < M:
        continue

    word_dict[word] -= 1
word_dict = sorted(word_dict, key=lambda x: (word_dict[x], -1 * len(x), x))

for word in word_dict:
    print(word)
