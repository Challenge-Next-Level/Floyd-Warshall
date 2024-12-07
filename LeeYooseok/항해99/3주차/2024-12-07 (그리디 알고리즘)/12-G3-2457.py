N = int(input())
flower_list = list()
for _ in range(N):
    s_m, s_d, e_m, e_d = map(int, input().split())

    flower_list.append([s_m, s_d, e_m, e_d])

flower_list.sort()

# 가장 최근에 심은 꽃이 지는 날
latest_end = (3, 1)
answer = 0

idx = 0
while idx < N:
    flower = flower_list[idx]

    # 현재 idx번째 꽃을 이전에 심은 꽃과 함께 심을 수 있다면 -> 중간에 비어있는 날이 없다면
    if (flower[0], flower[1]) <= latest_end < (flower[2], flower[3]):
        # 현재 심을 수 있는 꽃들 중 가장 마지막에 지는 꽃 찾기
        max_end = (flower[2], flower[3])

        while idx < N - 1:
            new_flower = flower_list[idx + 1]

            # idx + 1번째 꽃을 심을 수 없다면
            if latest_end < (new_flower[0], new_flower[1]):
                break

            # 현재 심을 수 있는 꽃들 중 가장 마지막에 지는 꽃 찾기
            if max_end < (new_flower[2], new_flower[3]):
                max_end = (new_flower[2], new_flower[3])

            idx += 1

        # 찾은 꽃 심기
        answer += 1
        latest_end = max_end

        # 11월 30일 까지 모두 심었다면 종료
        if (11, 30) < latest_end:
            print(answer)
            exit()
    idx += 1

print(0)

