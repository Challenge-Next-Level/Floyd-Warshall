N = int(input())
stick_list = [int(input()) for _ in range(N)]

answer = list()

for i in range(N - 1, -1, -1):
    now_stick = stick_list[i]
    if answer:
        if answer[0] < now_stick:
            answer.insert(0, now_stick)
    else:
        answer.append(now_stick)

print(len(answer))
