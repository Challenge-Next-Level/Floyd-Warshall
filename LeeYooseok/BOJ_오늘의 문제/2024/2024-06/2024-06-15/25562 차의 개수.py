N = int(input())

# 서로 다른 차의 개수의 최댓 -> 등비수열 -> 모든 쌍의 차가 다른 값을 가짐 -> N(N-1) / 2
print(N*(N-1) // 2)
number = 1
for _ in range(N):
    print(number, end=' ')
    number *= 2
print()

# 서로 다른 차의 개수의 최소 -> 등차수열 -> N - 1
print(N-1)
number = 1
for _ in range(N):
    print(number, end=' ')
    number += 1