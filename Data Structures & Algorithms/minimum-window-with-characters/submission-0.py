class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) == 0 or len(t) == 0 or len(s) < len(t):
            return ""

        map_t = {}

        for i in range(len(t)):
            map_t[t[i]] = map_t.get(t[i], 0) + 1
         
        required = len(map_t)
        left = 0
        right = 0
        create = 0
        ans = [-1, 0, 0]
        substring_map = {}

        while right < len(s):
            c = s[right]
            substring_map[c] = substring_map.get(c, 0) + 1
            if c in map_t and substring_map[c] == map_t[c]:
                create += 1
            while left <= right and create == required:
                c = s[left]
                if ans[0] == -1 or right - left + 1 < ans[0]:
                    ans[0] = right - left + 1
                    ans[1] = left
                    ans[2] = right
                substring_map[c] -= 1
                if c in map_t and substring_map[c] < map_t[c]:
                    create -= 1
                left += 1 
            right += 1 
        if ans[0] == -1:
            return ""

        return s[ans[1]: ans[2] + 1]


        