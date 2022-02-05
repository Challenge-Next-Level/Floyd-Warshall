"""
- 피보나치 함수에서 fibo(0) 과 fibo(1)이 호출되는 횟수 출력
- fibo(n) = fibo(n-1) + fibo(n-2)
"""
t = int(input())

nums = list()
for _ in range(t):
    nums.append(int(input()))

dp_0 = [1, 0, 1]
dp_1 = [0, 1, 1]

for n in range(3, max(nums) + 1):
    dp_0.append(dp_0[n - 1] + dp_0[n - 2])
    dp_1.append(dp_1[n - 1] + dp_1[n - 2])

for n in nums:
    print(dp_0[n], dp_1[n])
