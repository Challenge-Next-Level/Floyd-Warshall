import sys

input = sys.stdin.readline

# 스위치를 눌렀을 때 상태 변경을 해주는 함수
def reverse(bulbs, count):
    for i in range(1, N-1):
        if bulbs[i-1] != target[i-1]:
            count += 1
            for j in range(i-1, i+2):
                bulbs[j] = not bulbs[j]
    # 마지막 전구만 따로 처리
    if bulbs[N-1] != target[N-1]:
        count += 1
        bulbs[N-2] = not bulbs[N-2]
        bulbs[N-1] = not bulbs[N-1]
    if bulbs == target:
        return count
    else:
        return -1


N = int(input())

# not을 이용해 간편하게 처리하고 싶어서 0:False, 1:True의 bool 값으로 바꾸었다.
off = list(map(bool, map(int, input().rstrip())))

# 0번째 스위치를 누른 상태를 저장하는 리스트
on = off.copy()
on[0] = not on[0]
on[1] = not on[1]

target = list(map(bool, map(int, input().rstrip())))

# 처음부터 상태가 같은 경우 스위치를 눌러줄 필요가 없으니 0 출력
if off == target:
    print(0)
else:
    # 0번째 전구를 안눌렀을 때
    count = reverse(off, 0)
    if count != -1:
        print(count)
    else:
        # 0번째 전구를 눌렀을 때
        count = reverse(on, 1)
        print(count if count else -1)