from itertools import combinations, product

def solution(dice):
    # 주사위 n개 -> n/2 로 짝을 지어서 가져간다. -> 주사위를 굴려서 나온 수를 다 합친 수가 더 크면 이긴다. -> 이길수있는 경우의 짝을 구해라.
    n = len(dice)
    A, result = [], []
    # n/2 개로 뽑는 경우의 짝
    cases = list(combinations(range(n), n // 2)) # 0 ~ n-1 까지의 수들을 n/2 개로 짝을 이룸

    for case in cases:
        dices = [dice[c] for c in case]
        nums = sorted([sum(i) for i in product(*dices)])
        A.append(nums)

    a, p = 0, len(A)
    for i in range(p):
        B = A[p - i - 1] # B와 A는 대칭의 구조

        # A를 사전에 정렬해 두고, A의 값을 돌면서 B보다 작은 횟수들을 모두 더해나 나가도록 이분탐색을 적용
        temp = 0 # A가 이기는 경우의 수
        for t in A[i]:
            # 즉, 이분탐색으로 A의 현재 수(t) 보다 작으면서 가장 큰 수를 찾음 -> t 보다 작은 수들의 개수 = A가 이기는 경우의 수
            left, right = 0, len(B) - 1
            while left <= right:
                mid = (left + right) // 2
                if B[mid] < t:
                    left = mid + 1
                else:
                    right = mid - 1
            temp += left

        # 가장 승리의 수가 높은 경우 반환
        if a < temp:
            a = temp
            result = [x + 1 for x in cases[i]]

    return result
