n = int(input())
developer = list(map(int, input().split()))

answer = 0
left, right = 0, n - 1
while left < right:
    answer = max(answer, (right - left - 1) * min(developer[left], developer[right]))
    if developer[left] > developer[right]:
        right -= 1
    else:
        left += 1
print(answer)