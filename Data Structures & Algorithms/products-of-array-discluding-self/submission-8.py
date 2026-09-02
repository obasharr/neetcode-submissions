class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)

        pre = 1
        post = 1

        for i in range(len(nums)):
            result[i] = pre
            pre = nums[i] * pre

        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * post
            post = post * nums[i]
        
        return result


        