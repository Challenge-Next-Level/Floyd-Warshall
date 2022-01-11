from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort() # O(n) 솔루션을 문제에서 요구했지만 귀찮다... 어렵기도 하고
        return nums


s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))