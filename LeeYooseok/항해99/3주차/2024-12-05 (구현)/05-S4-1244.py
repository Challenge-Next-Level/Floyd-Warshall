import sys

input = sys.stdin.readline

N = int(input())
switch_list = [0] + list(map(int, input().split()))

M = int(input())
for i in range(1, M + 1):
    sex, x = map(int, input().split())

    # 남학생 이면
    if sex == 1:
        for idx in range(x, N + 1, x):
            switch_list[idx] = abs(switch_list[idx] - 1)
    # 여학생 이면
    elif sex == 2:
        # 자기 자신 변경
        switch_list[x] = abs(switch_list[x] - 1)
        # 좌, 우 한계 확인
        left, right = x - 1, N - x
        for idx in range(1, min(left, right) + 1):
            # 대칭 확인 하면서, 스위치 전환
            if switch_list[x - idx] != switch_list[x + idx]:
                break

            switch_list[x - idx] = abs(switch_list[x - idx] - 1)
            switch_list[x + idx] = abs(switch_list[x + idx] - 1)

for i in range(1, N + 1, 20):
    print(*switch_list[i:min(i + 20, N + 1)])