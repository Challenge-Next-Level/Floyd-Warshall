import sys

input = sys.stdin.readline

N = int(input())

table = [[0 for _ in range(5)]]
table.extend([list(map(int, input().split())) for _ in range(N)])

answer = [0 for _ in range(N + 1)]

# 1번부터 N번 학생에 대하여
for i in range(1, N + 1):
    # 1학년부터 5학년까지 지내오면서 한번이라도 같은 반이었던 사람이 가장 많은 학생을 임시 반장으로
    class_mate_set = set()
    # 1학년부터 5학년에 대하여
    for j in range(5):
        now_class = table[i][j]
        for k in range(1, N + 1):
            if k == i:
                continue

            # 같은 반이었던 학생을 set에 추가한다.
            if now_class == table[k][j]:
                class_mate_set.add(k)
    answer[i] += len(class_mate_set)

max_num = max(answer)
for i in range(1, N + 1):
    if answer[i] == max_num:
        print(i)
        break
