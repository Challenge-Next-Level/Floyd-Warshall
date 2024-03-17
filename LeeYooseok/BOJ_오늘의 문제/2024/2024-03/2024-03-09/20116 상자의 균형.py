import sys

input = sys.stdin.readline

n, L = map(int, input().split())
x_loc_list = list(map(int, input().split()))

# 모든 1 ≤ i < n 에 대하여 i+1, i+2, ..., n 번 상자들의 무게 중심의 x좌표가 i번 상자의 구간 안에 포함되면 박스 전체가 균형
stable_list = x_loc_list[:]
for i in range(n - 1, 1, -1):
    stable_list[i - 1] = stable_list[i - 1] + stable_list[i]

# 균형을 이루는지 확인
for i in range(n - 1):
    avg_center = stable_list[i + 1] / (n - i - 1)

    if x_loc_list[i] - L < avg_center < x_loc_list[i] + L:
        continue
    else:
        print("unstable")
        exit()

print("stable")