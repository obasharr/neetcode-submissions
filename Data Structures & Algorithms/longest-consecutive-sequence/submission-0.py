class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        numSet = set(nums)
        longest = 1

        for num in numSet:
            if num - 1 in numSet:
                continue

            currentNum = num
            currentLen = 1

            while currentNum + 1 in numSet:
                currentNum += 1
                currentLen += 1
            
            longest = max(longest, currentLen)

        return longest
        