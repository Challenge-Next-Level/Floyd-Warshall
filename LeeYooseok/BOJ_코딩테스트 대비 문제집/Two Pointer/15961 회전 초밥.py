from collections import defaultdict

N, d, k, c = map(int, input().split())
dish_list = list()
for _ in range(N):
    dish_list.append(int(input()))

# 원형이므로 이어주기
dish_list.extend(dish_list)

left = 0
right = 0

_dict = defaultdict(int)

result = 0

# 쿠폰으로 주어지는 초밥은 무조건 먹기
_dict[c] += 1

# 1번 부터 k개의 초밥 먹기 (초기화)
while right < k:
    _dict[dish_list[right]] += 1
    right += 1

# 슬라이딩 윈도우 적용 (left, right 포인터 한칸씩 이동)
while right < len(dish_list):
    result = max(result, len(_dict)) # 결과값 업데이트

    # 1. 맨 왼쪽 초밥 제거
    _dict[dish_list[left]] -= 1

    # 2. 제거한 초밥의 개수가 0 이면, _dict 에서 제거
    if _dict[dish_list[left]] == 0:
        del _dict[dish_list[left]]

    # 3. 오른쪽 초밥 추가하기
    _dict[dish_list[right]] += 1

    # 포인터 이동
    left += 1
    right += 1

print(result)
