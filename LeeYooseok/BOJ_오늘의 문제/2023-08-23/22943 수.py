from itertools import permutations
k, m = map(int, input().split())
lst = []
MAX = 98765 // 10**(5-k)    # K개의 숫자를 고를 때 나올 수 있는 가장 큰 수

# 일단 최대 범위까지 소수 리스트 만들어 놓음
check = [0] * (MAX + 1)
prime_lst = set()   # 있는지 체크하기에는 set 자료형이 최고
for i in range(2, MAX+1):
    if check[i] == 0:
        check[i] = 1
        prime_lst.add(i)  # 1부터 N까지 소수 리스트
        j = 1
        while i * j <= MAX:
            check[i*j] = 1
            j+=1

# k개의 숫자 조합
for num in permutations(range(10), k):
    if num[0] == 0: # 첫 자리가 0이면 취급 안함
        continue
    N = int(''.join(list(map(str, num))))   # 숫자 조합
    temp = N
    while temp % m == 0:    # m으로 나누어떨어지지 않을 때까지 나눠줌
        temp //= m
    i = 2
    temp_lst = []
    while i <= int(temp**0.5):
        if temp % i == 0:   # 한 번이라도 소수와 소수가 아닌 수가 있어도 반례이므로 break 해줌
            if i in prime_lst and temp//i in prime_lst: # 2조건
                j = 2
                while j < N // 2:  # 1조건
                    if j in prime_lst and N-j in prime_lst:
                        lst.append(N)
                        break
                    j += 1
            break   #?
        i += 1

print(len(lst))