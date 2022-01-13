from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_num = 0
        for i in range(len(nums)): # 총 짝수의 개수
            if nums[i] % 2 == 0:
                even_num += 1
        check = 0 # 총 짝수의 개수만큼 탐색이 되었으면 배열은 제대로 정렬된 것
        end = len(nums) - 1 # 앞의 값과 바꿔야 되는 뒤 값의 index
        for i in range(len(nums)):
            if check == even_num: # 짝수를 모두 탐색했다면 종료
                break
            if nums[i] % 2 == 0: # 짝수를 보면 check + 1
                check += 1
                continue
            while nums[end] % 2 != 0: # 홀수를 보면 뒤에 있는 짝수와 swap
                end -= 1
            temp = nums[i]
            nums[i] = nums[end]
            nums[end] = temp
            check += 1
        return nums


s = Solution()
print(s.sortArrayByParity([3,1,2,4]))