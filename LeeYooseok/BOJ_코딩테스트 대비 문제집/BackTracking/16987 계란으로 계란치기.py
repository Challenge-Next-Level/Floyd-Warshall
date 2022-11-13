N = int(input())
egg_list = list()
broken_init = list()
for _ in range(N):
    S, W = map(int, input().split())
    egg_list.append([S, W])
    broken_init.append(S)

answer = 0


# 들고있는 계란, 깨져있는 계란 리스트
def egg_break(_egg, _broken, cnt):
    global answer
    if _egg == N:
        answer = max(answer, cnt)
        return
    # 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다.
    # 단, 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다.
    if _broken[_egg] > 0:
        visited = False
        for n in range(N):
            if n != _egg:
                if _broken[n] > 0:
                    visited = True
                    temp_broken = _broken[:]
                    temp_broken[n] -= egg_list[_egg][1]
                    temp_broken[_egg] -= egg_list[n][1]
                    temp_cnt = cnt

                    if temp_broken[n] <= 0:
                        temp_cnt += 1
                    if temp_broken[_egg] <= 0:
                        temp_cnt += 1

                    egg_break(_egg + 1, temp_broken, temp_cnt)

        if not visited:  # 모든 계란이 깨져 있다면,
            egg_break(_egg + 1, _broken, cnt)

    else:  # 손에 든 계란이 깨졌다면,
        egg_break(_egg + 1, _broken, cnt)


egg_break(0, broken_init, 0)
print(answer)
