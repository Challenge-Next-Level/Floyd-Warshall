import sys
input = sys.stdin.readline

M = int(input())

S = set()
answer = list()

for _ in range(M):
    operator_list = list(input().split())

    operator = operator_list[0]

    if operator == "add":
        x = int(operator_list[1])
        S.add(x)
    elif operator == "remove":
        x = int(operator_list[1])
        S.discard(x)
    elif operator == "check":
        x = int(operator_list[1])
        print(1 if x in S else 0)
    elif operator == "toggle":
        x = int(operator_list[1])
        S.remove(x) if x in S else S.add(x)
    elif operator == "all":
        S = set([i for i in range(1, 21)])
    elif operator == "empty":
        S.clear()
