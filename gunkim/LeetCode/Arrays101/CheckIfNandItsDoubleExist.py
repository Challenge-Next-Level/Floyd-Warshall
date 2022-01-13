class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i == j:
                    continue
                if arr[i] == arr[j] * 2:
                    return True
        return False