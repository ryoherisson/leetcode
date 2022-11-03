# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        res = 0

        l, r = 0, 0

        while r < len(s):
            while r < len(s) and hash_map.get(s[r], 0) == 0:
                hash_map[s[r]] = 1
                r += 1
            res = max(res, r - l)
            hash_map[s[l]] -= 1
            l += 1

        return res

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res
