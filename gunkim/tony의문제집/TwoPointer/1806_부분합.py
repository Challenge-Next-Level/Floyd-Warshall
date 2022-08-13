n, s = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0 # 좌,우 포인터
sumNums = nums[0] # 수들의 합
minLen = float('inf') # 최소 길이
while left <= right:
    if right == n:
        break
    if sumNums >= s:
        minLen = min(minLen, right-left+1)
        sumNums -= nums[left]
        left += 1
    else:
        right += 1
        if right == n:
            break
        sumNums += nums[right]

if minLen != float('inf'):
    print(minLen)
else:
    print(0)