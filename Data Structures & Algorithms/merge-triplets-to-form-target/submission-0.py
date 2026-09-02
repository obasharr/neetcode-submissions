class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        maxValues = [0] * 3

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                maxValues[0] = max(maxValues[0], triplet[0])
                maxValues[1] = max(maxValues[1], triplet[1])
                maxValues[2] = max(maxValues[2], triplet[2])

        return maxValues[0] == target[0] and maxValues[1] == target[1] and maxValues[2] == target[2]

