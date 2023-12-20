N, M = map(int, input().split())
people = [False for _ in range(N + 1)]

truth_list = set(input().split()[1:])

party_list = list()

for _ in range(M):
    party = set(input().split()[1:])

    party_list.append(party)

for _ in range(M):
    for party in party_list:
        if party & truth_list:
            truth_list = truth_list.union(party)

answer = 0
for party in party_list:
    if party & truth_list:
        continue
    answer += 1

print(answer)