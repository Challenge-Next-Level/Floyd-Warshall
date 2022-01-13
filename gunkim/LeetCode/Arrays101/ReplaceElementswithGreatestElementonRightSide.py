class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == len(arr) - 1: # 맨 끝은 -1
                arr[i] = -1
            else: # 우측 숫자 중 가장 큰 값
                arr[i] = max(arr[i + 1:])
        return arr