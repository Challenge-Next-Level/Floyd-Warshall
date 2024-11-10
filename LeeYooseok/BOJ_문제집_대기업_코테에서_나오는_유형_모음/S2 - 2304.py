N = int(input())

max_h, max_idx = 1, 0
pole_list = list()

for _ in range(N):
    L, H = map(int, input().split())

    if max_h <= H:
        max_h = H
        max_idx = L

    pole_list.append([L, H])

pole_list.sort()
answer = 0

# 앞에서부터 확인
now_idx, now_h = pole_list[0]
left_max_idx = max_idx
for idx, h in pole_list[1:]:
    if h == max_h:
        answer += ((idx - now_idx) * now_h)
        left_max_idx = idx
        break

    if h > now_h:
        answer += ((idx - now_idx) * now_h)
        now_idx = idx
        now_h = h

# 뒤에서부터 확인
pole_list.reverse()
now_idx, now_h = pole_list[0]
right_max_idx = max_idx
for idx, h in pole_list[1:]:
    if h == max_h:
        answer += ((now_idx - idx) * now_h)
        right_max_idx = idx
        break

    if h > now_h:
        answer += ((now_idx - idx) * now_h)
        now_idx = idx
        now_h = h


answer += ((right_max_idx + 1 - left_max_idx) * max_h)

print(answer)