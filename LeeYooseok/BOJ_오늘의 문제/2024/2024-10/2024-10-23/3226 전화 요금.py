N = int(input())

answer = 0

for _ in range(N):
    s = input()
    s = s.replace(":", " ")
    start_h, start_m, time = map(int, s.split())

    for i in range(time):
        h, m = start_h, start_m + i

        if m >= 60:
            h += (m // 60)
            m %= 60

        if 7 <= h <= 18:
            answer += 10
        else:
            answer += 5

print(answer)