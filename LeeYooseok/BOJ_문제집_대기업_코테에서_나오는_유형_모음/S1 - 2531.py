# set 과 list 슬라이싱을 활용한 풀이

N, d, k, c = map(int, input().split())

dish_list = list()
for _ in range(N):
    dish_list.append(int(input()))

answer = 0
for i in range(N):
    if i + k > N:
        now_type_cnt = len(set(dish_list[i:N] + dish_list[:(i +k) % N] + [c]))
    else:
        now_type_cnt = len(set(dish_list[i:i + k] + [c]))
    answer = max(answer, now_type_cnt)

print(answer)