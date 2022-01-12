from itertools import permutations

N = int(input())
a = []
for i in range(N): # 1 ~ N 까지 수를 리스트에 담는다
    a.append(i + 1)
per = list(permutations(a)) # 순열 값을 리스트로 만든다
for p in per: # 알맞게 출력한다
    print(' '.join(map(str, p)))