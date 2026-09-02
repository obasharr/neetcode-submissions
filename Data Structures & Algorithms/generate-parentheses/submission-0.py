class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.backTrack(ans, [], 0, 0, n)
        return ans


    def backTrack(self, ans, cur, open_count, close_count, max_count):
        if len(cur) == max_count * 2:
            ans.append("".join(cur))
            return
        if open_count < max_count:
            cur.append("(")
            self.backTrack(ans, cur, open_count + 1, close_count, max_count)
            cur.pop()
        if close_count < open_count:
            cur.append(")")
            self.backTrack(ans, cur, open_count, close_count + 1, max_count)
            cur.pop()
        