class Solution: # O(n)으로 해결해야 하는데 어떻게 해야할지 모르겠음. 일단 내 풀이로 해결.
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        distinct = []
        for i in range(len(nums)): # nums에 있는 숫자들을 중복되지 않게 distinct에 추가
            if len(distinct) == 0 or nums[i] != distinct[-1]:
                distinct.append(nums[i])
        distinct.sort() # distinct 정렬
        if len(distinct) < 3: # 3번 째로 큰 수 반환
            return distinct[-1]
        else:
            return distinct[-3]