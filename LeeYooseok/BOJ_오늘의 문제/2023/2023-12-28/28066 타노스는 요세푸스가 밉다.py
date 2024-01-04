from collections import deque

N, K = map(int, input().split())

animal = deque([i for i in range(1, N + 1)])

while K <= len(animal):
    animal.append(animal.popleft()) # 제거 후, 첫번째 청설모는 오른쪽 청설모
    for _ in range(K - 1):
        animal.popleft() # K - 1 마리의 청설모 제거

print(animal.popleft())
