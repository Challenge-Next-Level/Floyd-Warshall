from typing import List


# 중복 코드가 꼴보기 싫다... 일단 풀었으니 쉬자
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        INF = float('inf')
        count = 0
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                nums[i] = INF
                count += 1
                idx = i - 1
            elif nums[i] == nums[idx]:
                nums[i] = INF
                count += 1
        nums.sort()
        return len(nums) - count


s = Solution()
s.removeDuplicates([1,1,1,1])