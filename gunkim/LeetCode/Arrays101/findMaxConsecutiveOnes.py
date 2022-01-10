class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = -1
        answer = 0
        for i in range(len(nums) + 1): # 0을 탐색할 때 마다 이전 1이 얼마나 연속되는지 확인
            if i == len(nums) or nums[i] == 0:
                end = i
                if start == -1:
                    answer = max(answer, end)
                else:
                    answer = max(answer, end - start - 1)
                start = i
        return answer