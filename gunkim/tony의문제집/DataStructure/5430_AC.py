import sys
from collections import deque

t = int(sys.stdin.readline()[0]) # 테스트 케이스 수


def calculation(ch, st): # 연산자, 덱(dequeue)
    global isReverse
    if ch == 'D': # 버리기
        if len(st) == 0: # 덱이 비어있다면 False
            return False
        if isReverse == 1: # 역방향(뒤) 버리기
            st.pop()
        else: # 순방향(앞) 버리기
            st.popleft()
    elif ch == 'R': # 뒤집기
        if isReverse == 0:
            isReverse = 1
        else:
            isReverse = 0
    return True


for _ in range(t): # 테스트 때 마다 변수 초기화
    isReverse = 0
    case = sys.stdin.readline().split()[0]
    n = int(sys.stdin.readline()[0])
    stack = list(sys.stdin.readline()[1:-2].split(','))
    if stack[0] != '':
        stack = deque(map(int, stack))
    else:
        stack = []

    flag = 0
    for i in range(len(case)): # 함수 수행
        if calculation(case[i], stack) is False: # False 반환은 error 출력
            print('error')
            flag = 1
            break
    if flag == 0: # 모든 연산에서 True를 반환하면 덱 출력
        if isReverse == 1:
            stack.reverse()
        print('[' + ','.join(map(str, stack)) + ']')