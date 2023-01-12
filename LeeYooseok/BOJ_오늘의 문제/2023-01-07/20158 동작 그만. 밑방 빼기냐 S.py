N = int(input())
card_list = list(map(int, input().split()))

# 홀수, 짝수 누적합 구하기
mid = N // 2
odd, even = [0] + card_list[::2], [0] + card_list[1::2]
for idx in range(1, mid):
    odd[idx + 1] += odd[idx]
    even[idx + 1] += even[idx]
# 밑장빼기 안했을때 결과
answer = odd[-1]

for i in range(mid):
    temp_answer = odd[i] + (even[-2] - even[i])
    # 밑장빼기 한거
    answer = max(answer, temp_answer + card_list[-1])

    # 밑장배기 안한거
    answer = max(answer, temp_answer + card_list[i * 2])

print(answer)

