import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

start = 0
end = 0

answer = 0
visited = [False for _ in range(100001)]

while start <= end and end < N:
    if not visited[A[end]]:
        visited[A[end]] = True
        end += 1
        answer += end - start # end 와 start 사이에 있는 수를 뽑는 것 ?
    else:
        while visited[A[end]]:
            visited[A[start]] = False
            start += 1
print(answer)