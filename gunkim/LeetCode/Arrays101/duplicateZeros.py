from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0: # 0을 만나면 뒤에 복제 하면서 한 칸씩 뒤로 밀기
                before = 0
                for j in range(i + 1, len(arr)):
                    temp = arr[j]
                    arr[j] = before
                    before = temp
                i += 1
            i += 1


s = Solution()
s.duplicateZeros([1,0,2,3,0,4,5,0])