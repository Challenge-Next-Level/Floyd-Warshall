class Solution: # 한 번에 통과!
    def heightChecker(self, heights: List[int]) -> int:
        expected = []
        for i in range(len(heights)): # 리스트 복사
            expected.append(heights[i])
        expected.sort() # 복사한 리스트 정렬
        count = 0
        for i in range(len(heights)): # 원본과 복사본 비교
            if heights[i] != expected[i]:
                count += 1
        return count