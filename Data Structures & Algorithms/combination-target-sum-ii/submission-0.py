class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtrack(result, [], candidates, target, 0)
        return result

    def backtrack(self, result: List[List[int]], current: List[int], candidates: List[int], target: int, start: int):
        if target == 0:
            result.append(current.copy())
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if target - candidates[i] < 0:
                break
            current.append(candidates[i])
            self.backtrack(result, current, candidates, target - candidates[i], i + 1)
            current.pop()