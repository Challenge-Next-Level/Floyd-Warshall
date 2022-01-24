"""
- 임의의 회의 K는 회의 K-1 과 K+1과는 겹치고 다른 회의들 과는 겹치지 않는다.
- 모든 경우의 수 확인
    - 각 회의가 시작일때의 인원을 결과 리스트에 담는다
"""

n = int(input())

meets = list()

for _ in range(n):
    meets.append(list(map(int, input().split())))

# 정렬
meets.sort()

# 결과를 담을 리스트
peoples = list()

# 마지막 시작 값
last_start = max([s for s, e, p in meets])


# dfs 함수 : 끝이 아니라고 생각 시, 현재 값을 계속 더해준다.
def dfs(x, current):
    current += meets[x][2]  # 현재 회의의 인원수를 더함

    # 마지막 회의라고 생각시
    if meets[x][1] > last_start:
        peoples.append(current)
        return

    # 현재 회의 이후의 회의 시작 가능한지 확인
    for i in range(x+1, n):
        # 다음 회의 시작 시간이 현재 회의 종료 시간보다 빠를때
        if meets[x][1] > meets[i][0]:
            continue

        # 다음 회의 시작 시간이 현재 회의 종료 시간보다 이후일때
        dfs(i, current)


# 각 회의가 시작회의 일때의 경우의 수 확인
for i in range(n):
    dfs(i, 0)

print(max(peoples))

