# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in hash_map:
                if stack and stack[-1] == hash_map[c]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False
