n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left, right = 0, n-1
answer = [float('inf'), 0, 0]
while left < right:
    total = liquid[left] + liquid[right]
    if answer[0] > abs(total):
        answer = [abs(total), liquid[left], liquid[right]]
    if total < 0:
        left += 1
    elif total > 0:
        right -= 1
    else:
        break
print(answer[1], answer[2])