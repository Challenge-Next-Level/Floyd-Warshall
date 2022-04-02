"""
포인터 이동하면서 서로 다른 초밥 k개 담는 경우의 수 조사
안풀림
"""
import sys

input = sys.stdin.readline

# 접시 수, 초밥 종류, 연속해서 먹는 초밥 수, 쿠폰에 적힌 초밥 번호
N, d, k, c = map(int, input().split())

dishes = [int(input()) for _ in range(N)]

end = 0
result = 0

now_dishes = [dishes[0]]
num_dishes = 1

for start in range(N):
    while num_dishes < k:
        if dishes[end+1] not in now_dishes:
            num_dishes += 1
            now_dishes.append(dishes[end+1])
            end += 1
            if end == N-1:
                end = -1
        else:
            break

    total = len(now_dishes)

    if c in now_dishes:
        result = max(total, result)
    else:
        result = max(total + 1, result)

    now_dishes.pop(0)
    num_dishes -= 1


print(result)