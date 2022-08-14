import sys

N, S = map(int, input().split())

num_list = list(map(int, input().split()))

tmp_list = [0]
for idx in range(N):
    tmp_list.append(tmp_list[-1] + num_list[idx])

left = 1
right = 1

answer = sys.maxsize

while right < N+1:
    if (tmp_list[right] - tmp_list[left - 1]) >= S:
        answer = min(answer, (right - left + 1))
        left += 1
    else:
        right += 1

if answer == sys.maxsize:
    print(0)
else:
    print(answer)