#  1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19

E, S, M = map(int, input().split())

answer = 1

while True:
    if (answer - E) % 15 == 0 and (answer - S) % 28 == 0 and (answer - M) % 19 == 0:
        print(answer)
        exit()
    else:
        answer += 1