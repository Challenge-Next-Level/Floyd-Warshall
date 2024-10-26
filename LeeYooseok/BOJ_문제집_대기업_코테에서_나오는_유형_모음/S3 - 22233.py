import sys

input = sys.stdin.readline

N, M = map(int, input().split())

keyword_set = set([input().rstrip() for _ in range(N)])

for _ in range(M):
    keyword_list = list(input().rstrip().split(","))
    for k in keyword_list:
        keyword_set.discard(k)

    print(len(keyword_set))