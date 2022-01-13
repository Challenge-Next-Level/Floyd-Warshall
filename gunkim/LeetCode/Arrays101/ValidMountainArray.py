class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        while i < len(arr) - 1 and arr[i] < arr[i + 1]: # 엄격하게 증가
            i += 1
        if i == 0 or i == len(arr) - 1: # 한 번도 오르지 않거나 이미 다 올랐다면 False
            return False
        while i < len(arr) - 1 and arr[i] > arr[i + 1]: # 엄격하게 감소
            i += 1
        if i == len(arr) - 1: # 다 올랐다면 True
            return True
        return False