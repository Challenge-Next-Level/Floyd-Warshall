# 내 본 풀이는 '메모리 초과'가 발생하는 무식한 완전 탐색이었음
# 주의: python3는 '시간 초과' 발생, pypy3로 실행해야 함
import sys

n = int(sys.stdin.readline())  # 학생 수
arr = list(map(int, sys.stdin.readline().split()))  # 학생 코딩 실력
arr.sort()

# 해당 점수에 해당하는 학생 수 얻기
dict = {}
for i in range(n):
    if arr[i] not in dict:
        dict[arr[i]] = 1
    else:
        dict[arr[i]] += 1

result = 0
# 학생 한 명을 기준으로 나머지 두 학생에 대해 투 포인터 탐색
for i in range(n-2):
    # 무조건 포인터는 기준 학생 이후로 잡아야 함
    left, right = i + 1, n - 1
    while left < right: # left, right는 같을 수 없음
        total = arr[left] + arr[right] + arr[i]
        # <핵심!> 점수 총합이 0인 경우(같은 값이 있는 것에 대한 처리 필요)
        if total == 0:
            if arr[left] == arr[right]: # left와 right 같은 경우 해당 범위 저장
                result += (right - left)
            else: # 다른 경우 right 값에 대한 개수 합
                result += dict[arr[right]]
            left += 1
        elif total > 0: # 총합이 0 보다 큰 경우
            right -= 1
        elif total < 0: # 총합이 0 보다 작은 경우
            left += 1

print(result)