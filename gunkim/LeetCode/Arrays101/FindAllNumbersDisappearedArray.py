from typing import List
from collections import Counter

class Solution: # O(n)으로 해결해야 함. 근데 내 코드가 O(n)인 줄 모르겠음...ㅋㅋㅋ
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        c = Counter(nums) # Counter는 O(n)이라 함
        answer = []
        for i in range(1, len(nums) + 1): # 1~n 탐색시 없는 숫자는 answer에 추가
            if i not in c:
                answer.append(i)
        return answer



s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))