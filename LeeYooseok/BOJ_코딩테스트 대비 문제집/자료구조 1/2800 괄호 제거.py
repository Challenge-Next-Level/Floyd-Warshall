import itertools

expression = list(input())

opens = list()
pairs = list()

i = 0
for e in range(len(expression)):
    if expression[e] == "(":
        opens.append(e)
    elif expression[e] == ")":
        open_ = opens.pop()
        pairs.append([open_, e])

result = set()

for i in range(1, len(pairs)+1):
    comb = itertools.combinations(pairs, i)
    for j in comb:
        sub_expression = expression[:]
        for k in list(j):
            sub_expression[k[0]] = ''
            sub_expression[k[1]] = ''
        result.add(''.join(map(str, sub_expression)))

for i in sorted(result):
    print(i)