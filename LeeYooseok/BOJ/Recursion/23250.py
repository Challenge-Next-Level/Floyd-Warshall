# 기본적인 재귀 사용시 시간초과 발생

n, k = map(int, input().split())
t = 0


# n : 옮기려는 원반의 수
# from_pos : 옮길 원반이 현재 있는 출발점 기둥
# to_pos : 원반을 옮길 도착점 기둥
# aux_pos : 옮기는 과정에서 사용할 보조 기둥
def hanoi(n, from_pos, to_pos, aux_pos):
    global t
    if n == 1:  # 원반 1개를 옮기는 문제면 그냥 옮기면 됨
        t += 1
        if t == k:
            print(from_pos, to_pos)
        return

    # 원반 n-1개를 aux_pos 로 이동(to_pos 를 보조 기둥)
    hanoi(n - 1, from_pos, aux_pos, to_pos)

    # 가장 큰 원반을 목적지로 이동
    t += 1
    if t == k:
        print(from_pos, to_pos)
        return

    # aux_pos 에 있는 원반 n-1개를 목적지로 이동 (from_pos 를 보조 기둥)
    hanoi(n - 1, aux_pos, to_pos, from_pos)


hanoi(n, 1, 3, 2)
