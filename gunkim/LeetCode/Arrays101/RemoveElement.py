from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == val: # 제거하는 숫자는 -1로 변환
                nums[i] = -1
                count += 1
        nums.sort(reverse=True) # -1인 숫자들을 뒤로 보내기 위해 reverse sort
        return len(nums) - count


s = Solution()
s.removeElement([3,2,2,3], 3)