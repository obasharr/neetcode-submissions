class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        self.backtrack(target, res, combination, 0, nums)

        return res
    
    def backtrack(self, target: int, res: List[List[int]], combination: List[int], start: int, nums: List[int]):
        if target == 0:
            res.append(combination.copy())
        elif target < 0:
            return 
        for i in range(start, len(nums)):
            combination.append(nums[i])
            self.backtrack(target - nums[i], res, combination, i, nums)
            combination.pop()
