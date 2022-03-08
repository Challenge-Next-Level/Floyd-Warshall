# https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-12015-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-2-%EA%B3%A8%EB%93%9C2-%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89

n = int(input())
nums = list(map(int, input().split()))

arr = [0]

for n in nums:
    if arr[-1] < n:
        arr.append(n)
    else:
        # 이분탐색으로 해당 값을 넣어 줄 자리를 찾는다.
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < n:
                left = mid + 1
            else:
                right = mid

        arr[right] = n

print(len(arr) - 1)
