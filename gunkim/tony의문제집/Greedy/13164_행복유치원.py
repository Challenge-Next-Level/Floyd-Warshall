# 그룹을 나눌 수 있는 경우를 combinations로 찾아 풀었었다. 그러나 메모리 초과
# 그냥 머리가 존나 좋았어야 했다. 아이디어 구현 문제.
n, k = map(int, input().split())
people = list(map(int, input().split()))

diff = []
for i in range(n-1):
    diff.append(people[i+1] - people[i])
diff.sort()
# 총 n-1 개의 차이가 있을 것
# 우린 k-1개의 차이를 제거하게 된다. 3그룹으로 나눠 보면 끊기는 지점은 2곳. 즉, 2개의 차이를 제거 가능하다.
# 그럼 총 (n-1) - (k-1) = n-k 개의 차이가 있을 것이다.
print(sum(diff[:n-k]))