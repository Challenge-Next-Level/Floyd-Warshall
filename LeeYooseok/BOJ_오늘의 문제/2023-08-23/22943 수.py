K, M = map(int, input().split())

# K 자리의 소수 ->
n = 100000
# 0, 1, 2
a = [False, False] + [True] * (n - 2)

primes = list()

for i in range(2, n):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n, i):
            a[j] = False

prime_2_sum = set()

# for p_i_1 in range(len(primes)):
#     for p_i_2 in range(p_i_1 + 1, len(primes)):
#         prime_2_sum.add(primes[p_i_1] + primes[p_i_2])
#
# print(prime_2_sum)
