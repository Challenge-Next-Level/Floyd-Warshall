import sys

input = sys.stdin.readline

N, M = map(int, input().split())
duid_list = set([input().strip() for _ in range(N)])

answer_list = list()

for _ in range(M):
    bo = input().strip()
    if bo in duid_list:
        answer_list.append(bo)

print(len(answer_list))
answer_list.sort()
for a in answer_list:
    print(a)