from collections import deque

S = input()

deq = deque(list())

status = "close"

for s in S:
    # 열린 괄호가 들어왔지만, 현재 닫혀 있을 때, -> 그 사이의 단어를 반대로 출력
    if s == "<" and status == "close":
        while deq:
            print(deq.pop(), end="")
        print("<", end="")
        status = "open"
    # 닫힌 괄호가 들어왔고, 현재 열려있을 때, -> 그 사이의 단어를 원래 순서로 출력
    elif s == ">" and status == "open":
        while deq:
            print(deq.popleft(), end="")
        print(">", end="")
        status = "close"
    # 공백이 들어왔고, 현재 닫혀있을 때, -> 그 사이의 단어를 반대로 출력
    elif s == " " and status == "close":
        while deq:
            print(deq.pop(), end="")
        print(" ", end="")
    # 이외의 경우 deque 에 추가
    else:
        deq.append(s)

# 나머지 잔여 문자 출력
while deq:
    print(deq.pop(), end="")



