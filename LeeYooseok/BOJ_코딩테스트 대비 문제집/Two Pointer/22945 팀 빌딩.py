N = int(input())
N_list = list(map(int, input().split()))

start = 0
end = N - 1
answer = 0

while start + 1 < end:
    answer = max(answer, (end - start - 1) * min(N_list[start], N_list[end]))

    # 포인터의 이동으로 개발자의 수는 무조건 감소한다.
    # 즉, 양 끝 개발자 능력이 덜 감소하는 쪽으로 이동한다.
    if N_list[start] < N_list[end]:
        start += 1
    else:
        end -= 1

print(answer)