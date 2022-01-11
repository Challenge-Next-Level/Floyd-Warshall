from typing import List


# in-place하게 해결하려면 아이디어가 필요함, 나에겐 어려웠다
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 큰 값을 비교해서 nums1 뒤부터 채우기
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        # 남은 것들 채우기
        nums1[:n] = nums2[:n]
        return


s = Solution()
print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3))