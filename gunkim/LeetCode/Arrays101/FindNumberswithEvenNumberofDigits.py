class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            count = 0
            while num > 0: # 10으로 0이 될 때까지 나눈 횟수를 카운트
                num //= 10
                count += 1
            if count % 2 == 0: # 카운트 값이 짝수면 정답 +1
                answer += 1
        return answer