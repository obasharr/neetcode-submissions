class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.backtrack(result, [], nums, 0)
        return result

    def backtrack(self, result: List[List[int]], current: List[int], nums: List[int], start:int):
        result.append(current.copy())
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            current.append(nums[i])
            self.backtrack(result, current, nums, i + 1)
            current.pop()