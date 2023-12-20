N = int(input())
num_list = list(map(int, input().split()))
reverse_num_list = num_list[::-1]

increase_list = [1 for _ in range(N)]
decrease_list = [1 for _ in range(N)] # reverse_num_list 를 이용한 증가하는 수열

# 증가하는 수열의 길이를 찾는 과정에서 DP 를 활용한다.
for now in range(N):
    for chk in range(now):
        if num_list[now] > num_list[chk]:
            increase_list[now] = max(increase_list[now], increase_list[chk] + 1)
            # 현재 나 자신의 길이 vs 나보다 작은 수의 길이 + 1

        if reverse_num_list[now] > reverse_num_list[chk]:
            decrease_list[now] = max(decrease_list[now], decrease_list[chk] + 1)

decrease_list = decrease_list[::-1]

# 가장 긴 바이토닉 수열 길이 = max(증가하는 수열 길이[i] + 감소하는 수열 길이[i] - 1)
answer = 0
for i in range(N):
    answer = max(increase_list[i] + decrease_list[i] - 1, answer)

print(answer)