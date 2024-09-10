def solution(nums):
    answer = len(nums) // 2
    num_set = set(nums)
    return min(answer, len(num_set))