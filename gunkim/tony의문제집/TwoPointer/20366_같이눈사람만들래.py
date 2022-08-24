# python3 는 시간초과
# 의문점: 첫 번째 눈사람을 만드는 과정(반복문 2개 활용)은 지름이 같은 것으로 만들 수 있게 되지 않나?
# 왜 예외 처리를 안하지?
n = int(input())
snow = list(map(int, input().split()))

snow.sort()
answer = float('inf')
for i in range(n-1):
    for j in range(i+1, n):
        left, right = 0, n-1
        while left < right:
            if left == i or left == j:
                left += 1
                continue
            if right == i or right == j:
                right -= 1
                continue
            firstSnowman = snow[i] + snow[j]
            secondSnowman = snow[left] + snow[right]
            answer = min(answer, abs(firstSnowman - secondSnowman))
            if answer == 0:
                break
            if firstSnowman > secondSnowman:
                left += 1
            else:
                right -= 1
print(answer)