from itertools import permutations

def solution(numbers):
    # 가능한 모든 수를 다 만듦
    numbers = list(numbers)
    all_nums = list()
    for i in range(1, len(numbers) + 1):
        all_nums += list(map(''.join, permutations(numbers, i)))

    all_nums = list(set(list(map(int, all_nums))))

    max_num = max(all_nums)
    prime_nums = list()
    a = [False, False] + [True] * (max_num - 1)
    for i in range(2, max_num + 1):
        if a[i]:
            prime_nums.append(i)
            for j in range(2 * i, max_num + 1, i):
                a[j] = False

    answer = 0

    for num in all_nums:
        if num in prime_nums:
            answer += 1

    return answer