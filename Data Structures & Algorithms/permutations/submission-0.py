class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        self.backtrack(result, [], nums, used)
        return result

    def backtrack(self, result: List[List[int]], current: List[int], nums: List[int], used: List[bool]):
        if len(current) == len(nums):
            result.append(current.copy())
            return
        
        for i in range(len(nums)):
            if not used[i]:
                current.append(nums[i])
                used[i] = True
                self.backtrack(result, current, nums, used)
                used[i] = False
                current.pop()