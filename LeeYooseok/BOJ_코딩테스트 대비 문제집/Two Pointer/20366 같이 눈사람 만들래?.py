import sys

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

answer = sys.maxsize

for start_1 in range(N):
    for end_1 in range(N-1, 2, -1):
        if start_1 + 2 < end_1:
            snow_1 = N_list[start_1] + N_list[end_1]

            start_2 = start_1 + 1
            end_2 = end_1 - 1

            while start_2 < end_2:
                snow_2 = N_list[start_2] + N_list[end_2]
                answer = min(answer, abs(snow_1 - snow_2))

                # 정렬되어 있는 상태이기 때문에 0 보다 작으면 snow_2 의 크기를 줄여주어야 함
                if (snow_1 - snow_2) < 0:
                    end_2 -= 1
                else:
                    start_2 += 1

print(answer)