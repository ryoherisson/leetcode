# https://leetcode.com/problems/valid-palindrome/

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         new_str = ""

#         for c in s:
#             if c.isalnum():
#                 new_str += c.lower()

#         return s == reversed(new_str)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.is_alpha_num(s[left]):
                left += 1
            while left < right and not self.is_alpha_num(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    def is_alpha_num(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
