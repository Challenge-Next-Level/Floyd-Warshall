N = int(input())
student_list = list(map(int, input().split()))
student_list.sort()

answer = 0

# 1명 씩 고정 하고, 나머지 두명은 투포인터 로 찾는다.
for s in student_list:
    left = s + 1
    right = N - 1

    while left < right:
        tmp_sum = student_list[s] + student_list[left] + student_list[right]

        # 점수 총 합이 0 인 경우
        if tmp_sum == 0:
