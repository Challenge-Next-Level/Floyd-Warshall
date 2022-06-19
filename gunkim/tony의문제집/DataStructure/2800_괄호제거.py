# 내가 생각한 해결법
# 1. 괄호를 제거하는 모든 경우의 수
# 2. 나온 결과가 올바른 괄호를 가지고 있는지 판별(사실 이게 올바른 결과를 가지고 올 것 같지는 않음)
# 3. 판별로 나온 결과들 정렬

# 물론 구현도 못하고 실패, 내가 예전에 다른 사람의 풀이를 보고 만들었던 코드를 다시 내가 참고하고 풀었다
from itertools import combinations
import sys

sentence = list(*sys.stdin.readline().split())
left_bracket = []
pair_bracket = []

for i in range(len(sentence)):
    if sentence[i] == '(':
        left_bracket.append(i)
        sentence[i] = ''
    elif sentence[i] == ')':
        pair_bracket.append([left_bracket.pop(), i])
        sentence[i] = ''

answer = set()
for i in range(len(pair_bracket)):
    c = combinations(pair_bracket, i) # 괄호를 추가할 곳의 케이스
    for j in c:
        make_sentence = sentence[:]
        for l, r in j:
            make_sentence[l] = '('
            make_sentence[r] = ')'
        answer.add(''.join(make_sentence))

for a in sorted(answer):
    print(a)