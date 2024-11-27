import itertools

S = list(input())

# 괄호 쌍 위치 찾기
opens = list()
pairs = list()

for idx in range(len(S)):
    if S[idx] == "(":
        opens.append(idx)
    elif S[idx] == ")":
        open_idx = opens.pop()
        pairs.append([open_idx, idx])

answer = set()

# 괄호 쌍 페어를 제거하며 문자열 만들기
for i in range(1, len(pairs) + 1):
    comb = itertools.combinations(pairs, i)

    for j in comb:
        temp_s = S[:]
        for k in list(j):
            temp_s[k[0]] = ''
            temp_s[k[1]] = ''
        answer.add(''.join(map(str, temp_s)))

for i in sorted(answer):
    print(i)