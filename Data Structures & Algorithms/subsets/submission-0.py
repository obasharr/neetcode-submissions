class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.generateSubsets(0, nums, [], result)
        return result

    def generateSubsets(self, index: int, nums: List[int], current: List[int], result: List[List[int]]):
        result.append(current.copy())

        for i in range(index, len(nums)):
            current.append(nums[i])
            self.generateSubsets(i + 1, nums, current, result)
            current.pop()