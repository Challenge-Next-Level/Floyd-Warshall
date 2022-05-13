# 백준 알고리준 분류 힌트에 '백트래킹'이 있어서 첨에 탈출 조건을 하나 넣었는데
# 곰곰히 생각해보면 정확한 탈출 조건이 있을 수가 없다?고 생각해서 지우고 그냥 제출함. 성공
import sys
from itertools import permutations

n = sys.stdin.readline().split()
A = list(map(int, sys.stdin.readline().split()))
operand = list(map(int, sys.stdin.readline().split()))
o = []
for i in range(len(operand)):
    if i == 0:
        o += ['+'] * operand[i]
    elif i == 1:
        o += ['-'] * operand[i]
    elif i == 2:
        o += ['*'] * operand[i]
    elif i == 3:
        o += ['/'] * operand[i]

po = set(list(permutations(o, len(o)))) # 순열연산으로 연산자의 배치 경우를 만든다
max_val, min_val = -float('inf'), float('inf')
max_A, min_A = max(A), min(A)
for p in po: # 연산자의 배치 경우의 수를 모두 계산한다
    res = A[0]
    length = len(p)
    for i in range(length):
        if p[i] == '/': # 음수 나눈셈의 경우 c++의 연산을 따라한다
            if res < 0 and A[i + 1] < 0:
                res = abs(res) // abs(A[i + 1])
            elif res < 0 or A[i + 1] < 0: # 둘 중 하나만 음수일 때 몫 음수
                res = -1 * (abs(res) // abs(A[i + 1]))
            else:
                res //= A[i + 1]
        elif p[i] == '+':
            res += A[i + 1]
        elif p[i] == '-':
            res -= A[i + 1]
        elif p[i] == '*':
            res *= A[i + 1]

        if i == length - 1:
            max_val = max(max_val, res)
            min_val = min(min_val, res)

print(max_val)
print(min_val)