import sys

input = sys.stdin.readline

N, K = map(int, input().split())

country_list = list()
for _ in range(N):
    country_index, gold, silver, bronze = map(int, input().split())
    country_list.append([gold, silver, bronze, country_index])

country_list.sort(reverse=True)

grade, s = 1, 0
for i in range(N):
    if i > 0:
        if country_list[i - 1][:3] == country_list[i][:3]:
            s += 1  # 공통 등수 개수
        else:
            if s > 0:
                grade += s
                s = 0
            grade += 1
    if country_list[i][3] == K:
        print(grade)
        break
