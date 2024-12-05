from collections import deque

# Deque 을 사용하기로 했다.
N, K = map(int, input().split())
people_list = deque([(i + 1) for i in range(N)])

answer = list()
while people_list:
    for i in range(K - 1):
        people_list.append(people_list.popleft())
    answer.append(people_list.popleft())


answer = str(answer)
answer = answer.replace("[", "<").replace("]", ">")

print(answer)